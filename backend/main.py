from fastapi import FastAPI
from app.api import route_upload,  route_documentlist, route_ask
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PDF Q&A Chatbot API", description="A local-first RAG chatbot API that lets you chat with your documents. Built with React, FastAPI, LangChain, and Ollama — 100% open-source, runs fully offline with no data leaving your machine.")

app.add_middleware(
    CORSMiddleware,
    allow_origins = ["http://localhost:5173"],
    allow_methods = ["*"],
    allow_headers = ["*"]
)

app.include_router(route_upload.router)
app.include_router(route_documentlist.router)
app.include_router(route_ask.router)

@app.get("/")
def heanth_check():
    return {'status' : 200, 'message' : 'Health check success'}




