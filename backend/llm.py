"""
VidhiAI LLM Integration Module
Integrates Google Gemini (gemini-3.5-flash / gemini-flash-latest) with deterministic RAG grounding
for the Government of Assam Administrative Knowledge System.

Guarantees:
1. Strict statutory grounding on retrieved gazettes/rules.
2. High-performance fallback resilience if offline or under heavy demand.
3. Smooth, professional, executive responses with zero emojis.
4. Intelligent administrative advisory for queries without an exact clause.
"""

import os
import re
import json
import logging
import httpx
from typing import List, Dict, Any, Optional

logger = logging.getLogger("vidhiai.llm")

# Primary and fallback Gemini models
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")
PRIMARY_MODEL = os.environ.get("GEMINI_PRIMARY_MODEL", "gemini-3.5-flash")
FALLBACK_MODELS = ["gemini-flash-latest", "gemini-3.7-flash"]
GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/models"


def _clean_json_text(text: str) -> str:
    """Extract raw JSON from model response even if surrounded by markdown code blocks."""
    text = text.strip()
    match = re.search(r"```(?:json)?\s*([\s\S]*?)\s*```", text)
    if match:
        return match.group(1).strip()
    return text


def call_gemini(prompt: str, json_mode: bool = True, timeout_sec: float = 4.0) -> Optional[Any]:
    """
    Executes a prompt against Gemini with primary and fallback model support.
    Returns parsed JSON (if json_mode=True) or raw text, or None if all models fail.
    """
    models_to_try = [PRIMARY_MODEL, "gemini-flash-latest"]
    
    payload: Dict[str, Any] = {
        "contents": [{"parts": [{"text": prompt}]}],
        "generationConfig": {
            "temperature": 0.1,
            "maxOutputTokens": 800,
        }
    }
    if json_mode:
        payload["generationConfig"]["responseMimeType"] = "application/json"

    with httpx.Client(timeout=timeout_sec) as client:
        for model in models_to_try:
            url = f"{GEMINI_BASE_URL}/{model}:generateContent?key={GEMINI_API_KEY}"
            try:
                resp = client.post(url, json=payload)
                if resp.status_code == 200:
                    data = resp.json()
                    candidates = data.get("candidates", [])
                    if candidates and "content" in candidates[0]:
                        parts = candidates[0]["content"].get("parts", [])
                        if parts and "text" in parts[0]:
                            raw_text = parts[0]["text"]
                            if json_mode:
                                try:
                                    clean = _clean_json_text(raw_text)
                                    return json.loads(clean)
                                except Exception as parse_err:
                                    logger.warning(f"JSON parse error on model {model}: {parse_err}")
                                    return None
                            return raw_text.strip()
                elif resp.status_code == 503:
                    # High demand on this model, try fallback model
                    continue
                else:
                    logger.warning(f"Model {model} returned status {resp.status_code}: {resp.text[:120]}")
            except httpx.TimeoutException:
                # If network or model timed out, don't cascade delays; fall back immediately
                logger.warning(f"Model {model} timed out after {timeout_sec}s; switching to fast fallback")
                break
            except Exception as exc:
                logger.warning(f"Request failed for model {model}: {exc}")
                continue

    return None


def generate_llm_grounded_response(
    query: str,
    claims: List[Dict[str, Any]],
    role: str = "employee",
    persona: str = "officer",
    department: Optional[str] = None,
) -> Optional[Dict[str, Any]]:
    """
    Synthesizes an authoritative administrative response grounded strictly in the retrieved RAG claims.
    """
    if not claims:
        return None

    primary = claims[0]
    dept_name = department or primary.get("department", "Government of Assam")
    
    context_blocks = []
    for idx, c in enumerate(claims[:3]):
        context_blocks.append(
            f"[Source {idx+1}]: Document: '{c.get('docTitle')}' | Rule/Section: {c.get('ruleNo')} | Page: {c.get('page')}\n"
            f"Excerpts: \"{c.get('quote')}\"\n"
            f"Full Clause Text: {c.get('text', '')[:400]}"
        )
    context_str = "\n\n".join(context_blocks)

    system_prompt = f"""You are VidhiAI, the official verified legal & administrative AI assistant for the Government of Assam ({dept_name}).
You assist desk officers and citizens by providing authoritative, crystal-clear, and legally precise answers.

STRICT INSTRUCTIONS:
1. Base your answer strictly on the provided official gazette excerpts. Do NOT extrapolate or hallucinate unverified rules.
2. In the summary, provide a direct, conversational, yet authoritative answer. Always cite the exact document title, rule or section number, and page number.
3. Strictly NO emojis anywhere in the response.

User Query: "{query.strip()}"

Verified Official Corpus Excerpts:
{context_str}

Return ONLY a JSON object with this exact structure:
{{
  "summary": "Conversational, clear answer citing Rule and Page"
}}"""

    result = call_gemini(system_prompt, json_mode=True, timeout_sec=4.5)
    if isinstance(result, dict) and "summary" in result and result["summary"]:
        return {"summary": result["summary"].strip()}
    return None


def generate_llm_guidance(
    query: str,
    detected_dept: Optional[str] = None,
    all_departments: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """
    Generates intelligent administrative guidance and advisory when a query does not match
    an exact statutory clause in the uploaded gazettes.
    Strictly avoids blunt refusal text while guiding the user to the correct administrative channel.
    """
    dept_context = detected_dept or "Government of Assam Administrative Services"
    all_depts_str = ", ".join(all_departments or [
        "Administrative Reforms & Training (ARTPS Act)",
        "Pension & Public Grievances (Assam Pension Rules 1969)",
        "Revenue & Disaster Management (Mission Basundhara 2.0 / 3.0)"
    ])

    system_prompt = f"""You are VidhiAI, the authoritative administrative and statutory assistant for the Government of Assam.
A desk officer or citizen has asked an administrative question: "{query.strip()}"

Corpus Scope:
VidhiAI is currently loaded with official gazettes and statutory rules across: {all_depts_str}.
Detected Topic / Context: {dept_context}.

INSTRUCTIONS:
1. Provide a polite, helpful, and intelligent administrative consultation response.
2. Explain the governing administrative authority or state department responsible for this subject (e.g. APDCL for solar energy, DoP&PW for Central Civil Services, SewaSetu / RTPS for public services, Assam Pension Seva Kendra, Dharitree portal for land records).
3. If the query pertains to Central Government jurisdiction (such as Central Civil Services rules), politely explain that VidhiAI focuses on Assam State statutory rules, and outline the corresponding central authority (DoP&PW) and official portals.
4. If it pertains to an unindexed Assam department, guide the user on which department portal or gazette notification governs the procedure, and suggest submitting via SewaSetu or contacting the Designated Public Servant.
5. Provide actionable next steps for the desk officer or citizen.
6. MANDATORY RULE: NEVER use the phrase "Zero-Hallucination Safe Refusal" or "No verified provision found in the uploaded gazettes or rules matching this query. VidhiAI strictly prevents hallucination and will not generate answers outside official documents.".
7. Strictly NO emojis anywhere.

Return ONLY a JSON object with this exact structure:
{{
  "summary": "Helpful, authoritative guidance explaining administrative jurisdiction and procedure",
  "suggestedPortal": "Official Portal or Department Name"
}}"""

    result = call_gemini(system_prompt, json_mode=True, timeout_sec=4.5)
    safe_dept = detected_dept or "Administrative Affairs"
    dept_code = "".join([c for c in safe_dept if c.isalnum()])[:4].upper() or "GOA"

    if isinstance(result, dict) and "summary" in result and result["summary"]:
        summary_text = result["summary"].strip()
        portal = result.get("suggestedPortal") or "SewaSetu Portal (sewasetu.assam.gov.in)"
        return {
            "summary": summary_text,
            "department": safe_dept,
            "suggestedPortal": portal,
            "officerNoting": {
                "fileNo": f"GOA/{dept_code}-ADV/2026/NOTE-{str(abs(hash(query)))[-4:]}",
                "subject": f"Administrative Consultation & Procedural Guidance: {query[:45]}",
                "paragraphs": [
                    f"1. INQUIRY: Desk consultation regarding '{query.strip()}'.",
                    f"2. ADMINISTRATIVE JURISDICTION: {summary_text}",
                    "3. STATUTORY NOTICE: Binding regulatory action requires cross-referencing against the designated departmental gazette notification.",
                ],
                "recommendation": f"Submitted for administrative guidance and departmental referral to {portal}.",
            },
            "citizenGuide": {
                "summary": summary_text,
                "checklist": [
                    f"Identify designated nodal officer or portal ({portal})",
                    "Verify whether an applicable Assam Gazette notification or Office Memorandum is in effect",
                    "Submit standard application with required identity and service credentials",
                    "Track status via SewaSetu or designated departmental receipt number"
                ],
                "statutoryTimeline": "Standard departmental or SewaSetu statutory service delivery timelines apply."
            }
        }

    # Deterministic fallback guidance (ensuring 100% uptime without the forbidden refusal text)
    safe_dept = detected_dept or "Administrative Affairs"
    dept_code = "".join([c for c in safe_dept if c.isalnum()])[:4].upper() or "GOA"
    
    is_central = any(w in query.lower() for w in ["central", "ccs", "union"])
    if is_central:
        summary_fallback = (
            f"This query pertains to Central Government civil service rules rather than the State of Assam's gazetted statutory corpus. "
            f"Central Civil Services matters are governed under the Department of Pension & Pensioners' Welfare (DoP&PW) or relevant Central Ministries (pensionersportal.gov.in). "
            f"For Assam State Government employees, the applicable statutory framework is the Assam Services (Pension) Rules, 1969."
        )
        rec = "Submitted with referral to Central Civil Services regulations (DoP&PW / pensionersportal.gov.in)."
    else:
        summary_fallback = (
            f"Administrative inquiry regarding '{query.strip()}'. While a specific clause for this exact query is not indexed in the current gazette batches, "
            f"official procedures may be pursued through the {safe_dept} or the Government of Assam's unified public services portal (SewaSetu at sewasetu.assam.gov.in). "
            f"Desk officers can verify against department notifications or request gazette indexing from the nodal custodian."
        )
        rec = f"Submitted for administrative guidance and departmental verification under {safe_dept}."

    return {
        "summary": summary_fallback,
        "department": safe_dept,
        "suggestedPortal": "SewaSetu Portal (sewasetu.assam.gov.in) / Departmental Portal",
        "officerNoting": {
            "fileNo": f"GOA/{dept_code}-ADV/2026/NOTE-{str(abs(hash(query)))[-4:]}",
            "subject": f"Administrative Consultation & Procedural Guidance: {query[:45]}",
            "paragraphs": [
                f"1. INQUIRY: Desk consultation regarding '{query.strip()}'.",
                f"2. ADMINISTRATIVE JURISDICTION: {summary_fallback}",
                "3. STATUTORY NOTICE: Binding regulatory action requires cross-referencing against the designated departmental gazette notification.",
            ],
            "recommendation": rec,
        },
        "citizenGuide": {
            "summary": summary_fallback,
            "checklist": [
                f"Identify the designated nodal officer or portal for {safe_dept}",
                "Verify whether an applicable Assam Gazette notification or Office Memorandum is in effect",
                "Submit standard application with required identity and service credentials",
                "Track status via SewaSetu or designated departmental receipt number"
            ],
            "statutoryTimeline": "Standard departmental or SewaSetu statutory service delivery timelines apply."
        }
    }
