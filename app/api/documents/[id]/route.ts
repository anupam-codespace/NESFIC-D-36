import { NextRequest } from 'next/server';
import { deleteDocument, getDocumentById } from '@/lib/corpusService';

const BACKEND_URL = process.env.BACKEND_URL;

export async function DELETE(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
): Promise<Response> {
  const { id } = await params;

  if (BACKEND_URL) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 2000);

      const backendResponse = await fetch(`${BACKEND_URL}/api/documents/${encodeURIComponent(id)}`, {
        method: 'DELETE',
        headers: {
          'Content-Type': 'application/json',
        },
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

  const result = deleteDocument(id);
  if (!result) {
    return Response.json({ error: 'Document not found' }, { status: 404 });
  }

  return Response.json(result, { status: 200 });
}

export async function GET(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
): Promise<Response> {
  const { id } = await params;
  const doc = getDocumentById(id);
  if (!doc) {
    return Response.json({ error: 'Document not found' }, { status: 404 });
  }
  return Response.json(doc, { status: 200 });
}
