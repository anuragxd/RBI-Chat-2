from langgraph.graph import StateGraph, END
from backend.app.rag.state import RAGState
from backend.app.rag.chain import build_chain


retriever, chain = build_chain()


def retrieve_node(state: RAGState):
    docs = retriever.invoke(state["question"])
    state["context"] = "\n".join(d.page_content for d in docs)
    state["sources"] = ["RBI / Union Budget"] * len(docs)
    return state


def answer_node(state: RAGState):
    state["answer"] = chain.run(
        question=state["question"],
        context=state["context"]
    )
    return state


graph = StateGraph(RAGState)

graph.add_node("retrieve", retrieve_node)
graph.add_node("answer", answer_node)

graph.set_entry_point("retrieve")
graph.add_edge("retrieve", "answer")
graph.add_edge("answer", END)

rag_graph = graph.compile()