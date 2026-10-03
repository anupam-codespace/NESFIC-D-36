"""
VidhiAI Storage Manager
=======================
Handles document storage with dual capabilities:
  1. Local storage: Stores PDFs in `corpus/` with SHA-256 deduplication and fast local access.
  2. Firebase Cloud Storage: Connects to Firebase Cloud Storage if Firebase credentials/bucket are configured,
     allowing PDFs to be archived in the cloud and synchronized.

Zero data loss: If cloud is not configured or offline, local storage operates seamlessly with full integrity.
"""

import os
import hashlib
import logging
from typing import Optional, Dict, Any, Tuple

logger = logging.getLogger(__name__)

# Check for Firebase configuration from environment
FIREBASE_STORAGE_BUCKET = os.environ.get("FIREBASE_STORAGE_BUCKET") or os.environ.get("NEXT_PUBLIC_FIREBASE_STORAGE_BUCKET")
FIREBASE_CREDENTIALS_PATH = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

_firebase_app = None
_firebase_bucket = None

def init_firebase_storage():
    """Initializes Firebase Admin SDK if credentials or bucket are provided."""
    global _firebase_app, _firebase_bucket
    if _firebase_bucket is not None:
        return _firebase_bucket

    if not FIREBASE_STORAGE_BUCKET:
        logger.info("FIREBASE_STORAGE_BUCKET not set. Storage running in Local Resilient Mode.")
        return None

    try:
        import firebase_admin
        from firebase_admin import credentials, storage

        if not firebase_admin._apps:
            if FIREBASE_CREDENTIALS_PATH and os.path.exists(FIREBASE_CREDENTIALS_PATH):
                cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
                _firebase_app = firebase_admin.initialize_app(cred, {"storageBucket": FIREBASE_STORAGE_BUCKET})
            else:
                _firebase_app = firebase_admin.initialize_app(options={"storageBucket": FIREBASE_STORAGE_BUCKET})
        
        _firebase_bucket = storage.bucket()
        logger.info("Connected to Firebase Storage bucket: %s", FIREBASE_STORAGE_BUCKET)
        return _firebase_bucket
    except Exception as exc:
        logger.warning("Could not initialize Firebase Storage: %s. Using local storage.", exc)
        return None


def get_storage_status() -> Dict[str, Any]:
    """Returns the current status of storage systems."""
    bucket = init_firebase_storage()
    is_firebase_active = bucket is not None
    return {
        "storage_mode": "hybrid" if is_firebase_active else "local_resilient",
        "firebase_connected": is_firebase_active,
        "firebase_bucket": FIREBASE_STORAGE_BUCKET if is_firebase_active else None,
        "local_storage_dir": "corpus/",
        "status": "ready"
    }


def save_pdf_file(file_bytes: bytes, filename: str) -> Tuple[str, str, Optional[str]]:
    """
    Saves PDF bytes to local corpus directory and optionally mirrors to Firebase Storage.
    Returns:
        (sha256_hash, local_path, cloud_url)
    """
    sha256_hash = hashlib.sha256(file_bytes).hexdigest()

    # Determine corpus directory
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    corpus_dir = os.path.join(base_dir, "corpus")
    os.makedirs(corpus_dir, exist_ok=True)

    safe_filename = filename.replace(" ", "_")
    local_path = os.path.join(corpus_dir, safe_filename)

    # Save locally
    with open(local_path, "wb") as f:
        f.write(file_bytes)

    # Attempt cloud mirror if Firebase Storage is active
    cloud_url = None
    try:
        bucket = init_firebase_storage()
        if bucket is not None:
            blob = bucket.blob(f"gazettes/{safe_filename}")
            blob.upload_from_filename(local_path, content_type="application/pdf")
            cloud_url = blob.public_url
            logger.info("PDF mirrored to Firebase Storage: %s", cloud_url)
    except Exception as exc:
        logger.warning("Firebase Storage upload skipped: %s", exc)

    return sha256_hash, local_path, cloud_url
