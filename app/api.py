from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional, List

from app.agent import run_agent

app = FastAPI(title="Company AI Agent API")


class AskRequest(BaseModel):
    query: str
    session_id: Optional[str] = "default"


class AskResponse(BaseModel):
    answer: str
    source: List[str]


@app.post("/ask", response_model=AskResponse)
def ask_agent(request: AskRequest):
    result = run_agent(
        query=request.query,
        session_id=request.session_id
    )

    return AskResponse(
        answer=result["answer"],
        source=result["sources"]
    )
