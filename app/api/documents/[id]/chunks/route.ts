import { NextRequest } from 'next/server';
import { getDocumentChunks } from '@/lib/corpusService';

const BACKEND_URL = process.env.BACKEND_URL;

export async function GET(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
): Promise<Response> {
  const { id } = await params;

  if (BACKEND_URL) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 2000);

      const backendResponse = await fetch(`${BACKEND_URL}/api/documents/${encodeURIComponent(id)}/chunks`, {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
        cache: 'no-store',
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

  const result = getDocumentChunks(id);
  if (!result) {
    return Response.json({ error: 'Document not found' }, { status: 404 });
  }

  return Response.json(result, { status: 200 });
}
