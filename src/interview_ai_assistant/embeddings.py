from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings( model="nomic-embed-text")

def generate_embeddings(chunks: list[str]) -> list[list[float]]:
    return embeddings.embed_documents(chunks)
