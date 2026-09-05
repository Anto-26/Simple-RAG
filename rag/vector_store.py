from langchain_community.vectorstores import FAISS


class VectorStore:
    """Builds a FAISS index from document chunks and serves it as a retriever."""

    def __init__(self, embeddings):
        self.embeddings = embeddings
        self.store = None

    def build(self, chunks):
        self.store = FAISS.from_documents(chunks, self.embeddings)

    def as_retriever(self):
        if self.store is None:
            raise ValueError("Vector store has not been built yet")
        return self.store.as_retriever()
