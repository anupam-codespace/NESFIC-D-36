/**
 * Next.js Route Handler: /api/upload
 * Seamlessly handles file upload: proxies to FastAPI if running,
 * or runs native Next.js OCR indexing and deduplication engine if offline.
 */
import { NextRequest } from 'next/server';
import { uploadDocument } from '@/lib/corpusService';

const BACKEND_URL = process.env.BACKEND_URL;

export async function POST(request: NextRequest): Promise<Response> {
  let formData: FormData;
  try {
    formData = await request.formData();
  } catch (err) {
    return Response.json({ status: 'error', message: 'Invalid form data upload.' }, { status: 400 });
  }

  // If external backend is explicitly configured, try proxying with timeout
  if (BACKEND_URL) {
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3000);

      const backendResponse = await fetch(`${BACKEND_URL}/api/upload`, {
        method: 'POST',
        body: formData,
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

  // Native Next.js Fallback Engine for Vercel / serverless deployments
  try {
    const file = formData.get('file') as File | null;
    const title = (formData.get('title') as string) || (file ? file.name.replace(/\.[^/.]+$/, '') : 'Uploaded Gazette Document');
    const department = (formData.get('department') as string) || 'Administrative Reforms and Training Department (ARTPS)';
    const docType = (formData.get('doc_type') as string) || 'Statutory Circular';
    const authority = (formData.get('authority') as string) || 'Government of Assam';

    let buffer: Buffer | undefined;
    if (file) {
      const arrayBuffer = await file.arrayBuffer();
      buffer = Buffer.from(arrayBuffer);
    }

    const result = uploadDocument({
      filename: file ? file.name : 'official_gazette_upload.pdf',
      title,
      department,
      docType,
      authority,
      buffer,
    });

    if ('error' in result && result.status === 409) {
      return Response.json({ status: 'conflict', message: result.error }, { status: 409 });
    }

    return Response.json(result, { status: 200 });
  } catch (err) {
    return Response.json(
      { status: 'error', message: 'Document upload failed. Please verify the PDF format and try again.' },
      { status: 500 }
    );
  }
}
