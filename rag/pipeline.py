from .chunker import DocumentChunker
from .embedder import Embedder
from .loader import DocumentLoader
from .qa import QuestionAnswerer
from .vector_store import VectorStore


class RAGPipeline:
    """Wires the loader, chunker, embedder, vector store, and QA steps together."""

    def __init__(self, config):
        self.loader = DocumentLoader()
        self.chunker = DocumentChunker()
        self.embedder = Embedder(config.EMBEDDING_MODEL_NAME)
        self.vector_store = VectorStore(self.embedder.model)
        self.qa = QuestionAnswerer(config.CHAT_MODEL_NAME, config.GOOGLE_API_KEY)

    def process_document(self, file_path: str) -> int:
        documents = self.loader.load(file_path)
        chunks = self.chunker.split(documents)
        self.vector_store.build(chunks)
        return len(chunks)

    def ask(self, question: str) -> str:
        retriever = self.vector_store.as_retriever()
        return self.qa.answer(question, retriever)
