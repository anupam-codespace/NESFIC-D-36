import { NextRequest } from 'next/server';
import { askQuestion } from '@/lib/corpusService';

const BACKEND_URL = process.env.BACKEND_URL;

export async function POST(request: NextRequest): Promise<Response> {
  let body: {
    query?: string;
    role?: string;
    persona?: string;
    language?: string;
    document_id?: string;
    department?: string;
  };

  try {
    body = await request.json();
  } catch {
    body = { query: '' };
  }

  const query = (body.query || '').trim();

  // If external backend is explicitly configured, try proxying with timeout
  if (BACKEND_URL) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3000);

      const backendResponse = await fetch(`${BACKEND_URL}/api/ask`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(body),
        signal: controller.signal,
      });
      clearTimeout(timeoutId);

      if (backendResponse.ok) {
        const data = await backendResponse.json();
        return Response.json(data, { status: backendResponse.status });
      }
    } catch {
      // Fall through to native Next.js engine
    }
  }

  // Native Next.js Deterministic RAG Engine
  const result = askQuestion({
    query,
    role: body.role,
    persona: body.persona,
    language: body.language,
    document_id: body.document_id,
    department: body.department,
  });

  return Response.json(result, { status: 200 });
}
