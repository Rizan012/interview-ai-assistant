from qdrant_store import vector_store

def retrieve_similar_chunks(query: str) -> str | None:
    documents = vector_store.similarity_search_with_score(query, k=4)

    similar_chunks = ""
    seen_chunks = set()

    for document, score in documents:
        text = document.page_content.strip()

        if score >= 0.45 and text and text not in seen_chunks:
            similar_chunks += text + " "
            seen_chunks.add(text)

    return similar_chunks.strip() or None