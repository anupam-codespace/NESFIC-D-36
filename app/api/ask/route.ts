import { NextRequest } from 'next/server';

const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function POST(request: NextRequest): Promise<Response> {
  try {
    const body = await request.json();

    const backendResponse = await fetch(`${BACKEND_URL}/api/ask`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    const data = await backendResponse.json();
    return Response.json(data, { status: backendResponse.status });
  } catch (err) {
    return Response.json(
      {
        outcome: 'insufficient_evidence',
        query: '',
        claims: [],
        retrievedCount: 0,
        latencyMs: 0,
        auditId: 'ERR-BACKEND-OFFLINE',
        verifierStatus: 'ERROR (FastAPI Backend Unreachable)',
        error: String(err),
      },
      { status: 503 }
    );
  }
}
