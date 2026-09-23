from fastapi import APIRouter, HTTPException
from app.models.schemas import ResponseAsk, ResponseAskInformation, ResponseDocumentList
import os
from app.config import settings


router = APIRouter()

@router.post("/ask", response_model=ResponseAsk)
def ask(request: ResponseAskInformation):
    
    path_of_document = os.path.join(settings.upload_dir)
    files = [file for file in os.listdir(path_of_document)] 
    
    if request.documentname not in files:
        raise HTTPException(400, f"File not found {request.documentname}, check the document if its getting listed in /listdocument API")
    
    return {"documentname" : request.documentname, "documentask" : request.documentask, "llmresponse": "LLM Response"}