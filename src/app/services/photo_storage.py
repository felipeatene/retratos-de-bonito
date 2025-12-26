import hashlib
from pathlib import Path
from datetime import datetime
from fastapi import UploadFile

STORAGE_ROOT = Path("storage/photos")

def calculate_hash(file: UploadFile) -> str:
    hash_sha256 = hashlib.sha256()
    file.file.seek(0)
    for chunk in iter(lambda: file.file.read(8192), b""):
        hash_sha256.update(chunk)
    file.file.seek(0)
    return hash_sha256.hexdigest()

def save_photo_file(file: UploadFile) -> tuple[str, str]:
    now = datetime.utcnow()
    year = str(now.year)
    month = f"{now.month:02d}"
    target_dir = STORAGE_ROOT / year / month
    target_dir.mkdir(parents=True, exist_ok=True)
    file_path = target_dir / file.filename
    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())
    return file.filename, str(file_path)
