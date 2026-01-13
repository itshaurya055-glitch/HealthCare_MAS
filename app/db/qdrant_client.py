from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient("localhost", port=6333)

client.recreate_collection(
    collection_name="patient_memory",
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)
