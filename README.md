# Enterprise RAG

Upload a document (PDF or TXT) and ask questions about it. FastAPI backend, plain HTML/JS frontend, LangChain, FAISS, and Gemini.

## Structure

```
main.py              FastAPI app: /api/upload, /api/ask, serves frontend/
config.py            API key + model names
rag/
  loader.py          DocumentLoader   - reads a file into LangChain Documents
  chunker.py         DocumentChunker  - splits documents into chunks
  embedder.py        Embedder         - local sentence-transformers embedding model
  vector_store.py    VectorStore      - builds/queries the FAISS index
  qa.py              QuestionAnswerer - retrieves context and asks Gemini
  pipeline.py        RAGPipeline      - wires the above together
frontend/            index.html, style.css, script.js
```

## Setup

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
2. Add your Gemini API key to `.env`:
   ```
   GOOGLE_API_KEY=your-key-here
   ```
3. Set the chat model in `config.py`:
   ```
   CHAT_MODEL_NAME = "gemini-1.5-flash"
   ```

## Run

```
uvicorn main:app --reload
```

Then open http://127.0.0.1:8000 in your browser.
