# VidhiAI Evaluation Benchmark Results

**Date:** October 2026  
**Jurisdiction:** Government of Assam  
**Corpus Size:** 10 Authentic Government Gazettes & Acts (100% Digital Text Layers)  
**Outcome Accuracy:** 100.0% (20/20)  
**Grounded Precision:** 100% (Deterministic Character-Level Substring Verification)  
**Hallucination Rate:** 0.0% (Zero Hallucination Protocol)  
**Average Latency:** 3692.1ms  

## Detailed Test Log

| ID | Query | Expected Outcome | Actual Outcome | Verifier Status | Latency |
|---|---|---|---|---|---|
| Q01 | How many years of service are required for family pension in Assam? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4846.4ms |
| Q02 | What is the maximum qualifying service ceiling for pension calculation? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4841.2ms |
| Q03 | What is the requirement for date of confirmation if net qualifying service is between 10 and 20 years? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4485.3ms |
| Q04 | Is date of confirmation required if net qualifying service exceeds 20 years in Assam? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 6770.5ms |
| Q05 | What form is required for service verification in Assam pension application? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4797.9ms |
| Q06 | What is the computational base for superannuation pension in Assam? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 5159.6ms |
| Q07 | What clearance certificate is needed from the Directorate of Estates? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4292.0ms |
| Q08 | Who attests the specimen signature and joint photograph for Assam pension? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4202.0ms |
| Q09 | What is the statutory deadline to file a First Appeal under ARTPS Act 2012? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4164.1ms |
| Q10 | What is the maximum time for the First Appellate Authority to dispose of an appeal under ARTPS? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4748.1ms |
| Q11 | What is the daily penalty amount imposed on a designated public servant for delayed public service under ARTPS Act 2012? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4459.8ms |
| Q12 | Can the First Appellate Authority extend the disposal deadline beyond 30 days under ARTPS? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 2531.6ms |
| Q13 | Which department notifies designated public authorities and service delivery timelines? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 4216.1ms |
| Q14 | What portal facilitates online appeals under the ARTPS Act in Assam? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 3184.3ms |
| Q15 | What is the land settlement ceiling for homestead purposes in municipal areas under Mission Basundhara 2.0? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 5285.6ms |
| Q16 | What is the settlement ceiling for agricultural land under Mission Basundhara 2.0? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 893.2ms |
| Q17 | What procedure confers ownership rights to rayats under Basundhara 2.0? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 1251.1ms |
| Q18 | What status is Mission Basundhara 3.0 notification under before administrative approval? | `answered` | `answered` | `PASSED (Deterministic Substring Match)` | 1053.8ms |
| Q19 | What is the government subsidy percentage for residential rooftop solar installation under Assam solar policy? | `insufficient_evidence` | `insufficient_evidence` | `REFUSED (SAFE - No Grounded Source Found)` | 1264.9ms |
| Q20 | Under Central Civil Services Pension Rules 2021, what is the maximum family pension amount? | `insufficient_evidence` | `insufficient_evidence` | `REFUSED (SAFE - Central Govt Jurisdiction Excluded)` | 1394.4ms |
