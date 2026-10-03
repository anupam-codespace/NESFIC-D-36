const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function GET(): Promise<Response> {
  try {
    const backendResponse = await fetch(`${BACKEND_URL}/api/documents`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      cache: 'no-store',
    });

    const data = await backendResponse.json();
    return Response.json(data, { status: backendResponse.status });
  } catch {
    return Response.json([], { status: 503 });
  }
}
