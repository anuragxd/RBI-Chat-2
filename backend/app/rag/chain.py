from langchain_classic.chains import LLMChain
from langchain_groq import ChatGroq
from backend.app.rag.prompts import RAG_PROMPT
from backend.app.rag.retriever import get_retriever

def build_chain():
    retriever = get_retriever()

    llm = ChatGroq(
        model_name="llama-3.3-70b-versatile",
        temperature=0
    )

    chain = LLMChain(
        llm=llm,
        prompt=RAG_PROMPT
    )

    return retriever, chain

