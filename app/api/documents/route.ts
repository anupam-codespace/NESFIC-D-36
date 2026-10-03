import { getDocuments } from '@/lib/corpusService';

const BACKEND_URL = process.env.BACKEND_URL;

export async function GET(): Promise<Response> {
  if (BACKEND_URL) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 2000);

      const backendResponse = await fetch(`${BACKEND_URL}/api/documents`, {
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

  // Native Next.js verified corpus list
  const docs = getDocuments();
  return Response.json(docs, { status: 200 });
}
