import uuid, os, magic
from datetime import datetime
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.config import settings
from app.models.schemas import UploadDocumentInfo, ResponseUploadDocument

router = APIRouter()

documents_db = {}

@router.post("/upload", response_model=ResponseUploadDocument)
async def upload_document(postfile: UploadFile = File(...)):
        """POST /upload
            - Accept a single file (PDF, DOCX, or TXT)
            - Validate file extension against allowed list; reject with 400 if unsupported
            - Validate file size against max limit; reject with 400 if too large
            - Generate a UUID as the document ID
            - Save the file to storage/uploads/ named as {uuid}{original_extension}
            - Store metadata (id, filename, path, upload_time, status="processing") in an in-memory dictionary — no database yet, that comes later
            - Return UploadResponse with status "processing" """
        file_type = magic.from_buffer(await postfile.read(2048), mime = True)
        
        if file_type not in settings.allowed_filetypes:
            raise HTTPException(400, {"error_details" : f"File format not allowed : {postfile.filename}"})
        
        extension = os.path.splitext(postfile.filename)[1].lower()
        await postfile.seek(0)
        content = await postfile.read()
        size_mb = len(content) / (1024 * 1024)
        
        if size_mb > settings.max_file_size:
            raise HTTPException(400, f"File too large {size_mb} MB!")
        
        doc_id = str(uuid.uuid4())[:5]
        doc_name = doc_id +"_"+str(postfile.filename)
        save_path = os.path.join(settings.upload_dir, f"{doc_name}")
        
        with open(save_path, "wb") as f:
            f.write(content)
              
        
        return ResponseUploadDocument(id=doc_id, filename= doc_name, status="uploaded")
        