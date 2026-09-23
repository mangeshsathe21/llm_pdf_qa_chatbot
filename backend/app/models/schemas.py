from pydantic import BaseModel, Field
from datetime import datetime


class UploadDocumentInfo(BaseModel):
    id: str
    filename: str
    upload_time: datetime
    status: str

class ResponseUploadDocument(BaseModel):
    id: str
    filename: str
    status: str

class ResponseDocumentList(BaseModel):
    documents : list[str]

class ResponseAskInformation(BaseModel):
    documentname: str
    documentask:str
    
class ResponseAsk(BaseModel):
    documentname: str
    documentask:str
    llmresponse: str