import os
from app.config import settings
from app.models.schemas import ResponseDocumentList, UploadDocumentInfo
from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get("/listdocument",response_model=ResponseDocumentList)
def list_document():
    """
    Return all documents currently in the upload folder as a DocumentListResponse
    """
    upload_folder_path = os.path.join(settings.upload_dir)
    uploaded_file_names = [filename for filename in os.listdir(upload_folder_path)]
    return ResponseDocumentList(documents=uploaded_file_names)