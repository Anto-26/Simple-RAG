from langchain_huggingface import HuggingFaceEmbeddings


class Embedder:
    """Wraps the local sentence-transformers model used to embed text."""

    def __init__(self, model_name: str):
        self.model = HuggingFaceEmbeddings(model_name=model_name)
