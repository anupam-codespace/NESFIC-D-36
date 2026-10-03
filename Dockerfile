# =====================================================================
# VidhiAI Production Containerfile (Deployable with Student Cloud Credits)
# DigitalOcean Droplet / Azure VM / Heroku / Render
# =====================================================================

FROM python:3.9-slim AS backend

WORKDIR /app

# Install system dependencies for PyMuPDF
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Install python dependencies
COPY backend/ backend/
COPY corpus/ corpus/
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy pydantic pymupdf pytest httpx

# Pre-seed database with all 10 official Assam gazettes
RUN PYTHONPATH=. python -m backend.seed

EXPOSE 8000

CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000"]
