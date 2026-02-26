from pathlib import Path
import pdfplumber
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from backend.core.config import DATA_DIR, VECTOR_DIR, EMBEDDING_MODEL
def ingest():
    docs = []

    for pdf in DATA_DIR.rglob("*.pdf"):
        with pdfplumber.open(pdf) as p:
            text = ""
            for page in p.pages:
                if page.extract_text():
                    text += page.extract_text() + "\n"

        docs.append(text)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks = []
    for d in docs:
        chunks.extend(splitter.split_text(d))

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

    db = FAISS.from_texts(chunks, embedding=embeddings)
    db.save_local(VECTOR_DIR)

    print("✅ Ingestion complete")


if __name__ == "__main__":
    ingest()