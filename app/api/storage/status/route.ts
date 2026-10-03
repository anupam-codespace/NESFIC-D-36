const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function GET(): Promise<Response> {
  try {
    const backendResponse = await fetch(`${BACKEND_URL}/api/storage/status`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      cache: 'no-store',
    });

    const data = await backendResponse.json();
    return Response.json(data, { status: backendResponse.status });
  } catch {
    return Response.json(
      {
        storage_mode: 'local_resilient',
        firebase_connected: false,
        firebase_bucket: null,
        local_storage_dir: 'corpus/',
        status: 'local_mode',
      },
      { status: 200 }
    );
  }
}
