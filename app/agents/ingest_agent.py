from app.embeddings.embedder import embed
from app.db.qdrant_client import client
import uuid

class IngestAgent:
    def run(self, text, metadata):
        vec = embed(text)
        client.upsert(
            collection_name="patient_memory",
            points=[{
                "id": str(uuid.uuid4()),
                "vector": vec,
                "payload": {
                    "text": text,
                    **metadata
                }
            }]
        )
