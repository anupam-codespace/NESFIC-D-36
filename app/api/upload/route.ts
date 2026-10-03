/**
 * Next.js Route Handler: /api/upload
 * Proxies multipart file upload to the FastAPI backend for OCR ingestion.
 */
import { NextRequest } from 'next/server';

const BACKEND_URL = process.env.BACKEND_URL ?? 'http://127.0.0.1:8000';

export async function POST(request: NextRequest): Promise<Response> {
  try {
    const formData = await request.formData();

    // Forward multipart form to FastAPI
    const backendResponse = await fetch(`${BACKEND_URL}/api/upload`, {
      method: 'POST',
      body: formData,
      // Do NOT set Content-Type — let fetch set the correct boundary
    });

    const data = await backendResponse.json();

    return Response.json(data, { status: backendResponse.status });
  } catch (err) {
    return Response.json(
      { status: 'error', message: 'Backend unreachable. Is the FastAPI server running?' },
      { status: 503 }
    );
  }
}
