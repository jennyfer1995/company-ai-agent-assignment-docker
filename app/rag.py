import os
import faiss
import numpy as np

DIM = 1536
index = faiss.IndexFlatL2(DIM)

documents = []
sources = []


def fake_embedding(text: str):
    np.random.seed(abs(hash(text)) % (2**32))
    return np.random.rand(DIM).astype("float32")


def load_docs():
    documents.clear()
    sources.clear()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    docs_path = os.path.join(base_dir, "documents")

    print("READING DOCUMENTS FROM:", docs_path)

    for f in os.listdir(docs_path):
        if f.endswith(".txt"):
            file_path = os.path.join(docs_path, f)
            with open(file_path, "r", encoding="utf-8") as file:
                text = file.read()

                print("LOADED FILE:", f)
                print("RAW LENGTH:", len(text))
                print("CONTENT PREVIEW:", repr(text[:100]))

                documents.append(text)
                sources.append(f)


def build_index():
    index.reset()
    for doc in documents:
        emb = fake_embedding(doc)
        index.add(np.array([emb]))


def retrieve_documents(query: str, k=2):
    query_lower = query.lower()

    # Rule-based filtering (enterprise-style)
    filtered = []

    for doc, source in zip(documents, sources):
        if "hr" in query_lower and "hr" in source.lower():
            filtered.append((doc, source))
        elif "security" in query_lower and "security" in source.lower():
            filtered.append((doc, source))
        elif "it" in query_lower and "it" in source.lower():
            filtered.append((doc, source))

    # If rule-based match found, return it
    if filtered:
        return filtered[:k]

    # Otherwise fallback to FAISS
    q_emb = fake_embedding(query)
    _, idx = index.search(np.array([q_emb]), k)

    return [(documents[i], sources[i]) for i in idx[0]]


# Load and index documents at startup
load_docs()
build_index()
