from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.core.config import VECTOR_DIR, EMBEDDING_MODEL


def get_retriever():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)
    db = FAISS.load_local(VECTOR_DIR, embeddings, allow_dangerous_deserialization=True)
    return db.as_retriever(search_kwargs={"k": 4})