from fastapi import APIRouter
from pydantic import BaseModel
from backend.app.rag.graph import rag_graph

router = APIRouter()


class ChatRequest(BaseModel):
    query: str


class ChatResponse(BaseModel):
    answer: str
    sources: list[str]


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    result = rag_graph.invoke({
        "question": req.query,
        "context": "",
        "answer": "",
        "sources": []
    })

    return ChatResponse(
        answer=result["answer"],
        sources=result["sources"]
    )