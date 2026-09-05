import os

from langchain_community.document_loaders import PyPDFLoader, TextLoader


class DocumentLoader:
    """Reads a file from disk into a list of LangChain Documents."""

    def load(self, file_path: str):
        suffix = os.path.splitext(file_path)[1].lower()
        if suffix == ".pdf":
            loader = PyPDFLoader(file_path)
        else:
            loader = TextLoader(file_path)
        return loader.load()
