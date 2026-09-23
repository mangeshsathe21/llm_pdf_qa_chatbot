from fastapi import FastAPI
from app.api import route_upload,  route_documentlist, route_ask

app = FastAPI(title="PDF Q&A Chatbot API")

app.include_router(route_upload.router)
app.include_router(route_documentlist.router)
app.include_router(route_ask.router)

@app.get("/")
def heanth_check():
    return {'status' : 200, 'message' : 'Health check success'}




