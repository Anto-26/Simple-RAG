from langchain.chains import RetrievalQA
from langchain_google_genai import ChatGoogleGenerativeAI


class QuestionAnswerer:
    """Answers a question by retrieving relevant chunks and asking Gemini."""

    def __init__(self, model_name: str, api_key: str):
        self.llm = ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)

    def answer(self, question: str, retriever) -> str:
        qa_chain = RetrievalQA.from_chain_type(llm=self.llm, retriever=retriever)
        result = qa_chain.invoke({"query": question})
        return result["result"]
