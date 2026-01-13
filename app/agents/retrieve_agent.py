from app.embeddings.embedder import embed
from app.db.qdrant_client import client

class RetrieveAgent:
    def run(self, query, patient_id):
        vec = embed(query)
        results = client.search(
            collection_name="patient_memory",
            query_vector=vec,
            limit=5,
            query_filter={
                "must": [{"key": "patient_id", "match": {"value": patient_id}}]
            }
        )
        return [r.payload["text"] for r in results]
