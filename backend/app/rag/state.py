from typing import TypedDict, List


class RAGState(TypedDict):
    question: str
    context: str
    answer: str
    sources: List[str]