from app.rag import retrieve_documents


def retrieve_policy_info(query: str):
    results = retrieve_documents(query)

    context_parts = []
    sources = []

    for doc_text, source in results:
        context_parts.append(
            f"Source: {source}\n{doc_text.strip()}"
        )
        sources.append(source)

    context = "\n\n".join(context_parts)

    return context, sources
