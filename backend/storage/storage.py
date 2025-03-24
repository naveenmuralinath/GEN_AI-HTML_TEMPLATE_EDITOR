import os
import shutil
from fastapi import UploadFile

UPLOAD_DIR = "backend/storage/templates"
os.makedirs(UPLOAD_DIR, exist_ok=True)

template_store = {}  # Store templates in memory

def save_template(file: UploadFile) -> dict:
    """Saves uploaded HTML templates."""
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    
    template_id = len(template_store) + 1
    template_store[template_id] = {"name": file.filename, "path": file_path}
    
    return {"template_id": template_id, "file_path": file_path}

def get_template(template_id: int) -> str:
    """Retrieves the stored HTML content."""
    if template_id not in template_store:
        return None

    file_path = template_store[template_id]["path"]
    
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return None
