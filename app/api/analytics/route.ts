const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function GET(): Promise<Response> {
  try {
    const backendResponse = await fetch(`${BACKEND_URL}/api/analytics`, {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      },
      cache: 'no-store',
    });

    const data = await backendResponse.json();
    return Response.json(data, { status: backendResponse.status });
  } catch {
    return Response.json({
      total_documents: 0,
      total_pages: 0,
      total_chunks: 0,
      approved_documents: 0,
      pending_documents: 0,
      department_distribution: [],
      document_metrics: [],
      total_queries: 0,
      answered_queries: 0,
      hallucination_rate: 0.0,
      verifier_pass_rate: 100.0,
    }, { status: 503 });
  }
}
