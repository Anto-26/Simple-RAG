from langchain.text_splitter import RecursiveCharacterTextSplitter


class DocumentChunker:
    """Splits documents into smaller, overlapping chunks for embedding."""

    def __init__(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )

    def split(self, documents):
        return self.splitter.split_documents(documents)
