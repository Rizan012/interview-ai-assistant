from pathlib import Path
from qdrant_client import QdrantClient, models
from langchain_qdrant import QdrantVectorStore
from embeddings import embeddings

QDB_PATH = Path(__file__).resolve().parents[2] / "qdrant_data"
COLLECTION_NAME = "interview_doc"

client = QdrantClient(path=str(QDB_PATH))

if not client.collection_exists(COLLECTION_NAME):
    vector_size = len(embeddings.embed_query("abc"))

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=models.VectorParams(
            size=vector_size,
            distance=models.Distance.COSINE,
        ),
    )

vector_store = QdrantVectorStore(
    client=client,
    collection_name=COLLECTION_NAME,
    embedding=embeddings,
)