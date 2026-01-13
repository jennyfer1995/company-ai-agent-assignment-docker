# app/memory.py

memory_store = {}

def get_memory(session_id: str):
    """
    Get conversation history for a session.
    """
    return memory_store.get(session_id, [])

def save_memory(session_id: str, history):
    """
    Save conversation history for a session.
    """
    memory_store[session_id] = history
