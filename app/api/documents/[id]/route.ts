import { NextRequest } from 'next/server';

const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function DELETE(
  _request: NextRequest,
  { params }: { params: Promise<{ id: string }> }
): Promise<Response> {
  try {
    const { id } = await params;
    const backendResponse = await fetch(`${BACKEND_URL}/api/documents/${encodeURIComponent(id)}`, {
      method: 'DELETE',
      headers: {
        'Content-Type': 'application/json',
      },
    });

    const data = await backendResponse.json();
    return Response.json(data, { status: backendResponse.status });
  } catch (err) {
    return Response.json({ error: 'Backend unreachable' }, { status: 503 });
  }
}
