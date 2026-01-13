import os
import logging

from app.llm_client import get_llm_client
from app.tools import retrieve_policy_info
from app.memory import get_memory, save_memory

logging.basicConfig(level=logging.INFO)

client = get_llm_client()


def decide_route(query: str):
    keywords = ["policy", "leave", "hr", "security", "internal"]
    return "TOOL" if any(k in query.lower() for k in keywords) else "LLM"


def run_agent(query: str, session_id: str):
    history = get_memory(session_id)
    route = decide_route(query)

    logging.info(f"Routing decision: {route}")

    if route == "TOOL":
        context, sources = retrieve_policy_info(query)
        answer = f"""
Based on Zero500 internal policy documents:

{context.strip()}
"""
    else:
        response = client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ]
        )
        answer = response.choices[0].message.content
        sources = []

    history.append({"user": query, "assistant": answer})
    save_memory(session_id, history)

    return {
        "answer": answer.strip(),
        "route": route,
        "sources": sources
    }
