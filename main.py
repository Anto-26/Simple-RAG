import os
import tempfile

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.staticfiles import StaticFiles

import config
from rag.pipeline import RAGPipeline

app = FastAPI(title="Enterprise RAG")

pipeline = RAGPipeline(config)


@app.post("/api/upload")
async def upload_document(file: UploadFile = File(...)):
    if not config.GOOGLE_API_KEY:
        raise HTTPException(status_code=400, detail="Missing GOOGLE_API_KEY in .env")

    suffix = os.path.splitext(file.filename)[1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(await file.read())
        tmp_path = tmp.name

    try:
        num_chunks = pipeline.process_document(tmp_path)
    finally:
        os.remove(tmp_path)

    return {"filename": file.filename, "chunks": num_chunks}


@app.post("/api/ask")
async def ask_question(question: str = Form(...)):
    if not config.CHAT_MODEL_NAME:
        raise HTTPException(status_code=400, detail="Missing CHAT_MODEL_NAME in config.py")
    if pipeline.vector_store.store is None:
        raise HTTPException(status_code=400, detail="Upload a document first")

    answer = pipeline.ask(question)
    return {"answer": answer}


app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
