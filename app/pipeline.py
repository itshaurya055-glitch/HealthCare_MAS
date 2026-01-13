from app.agents.ingest_agent import IngestAgent
from app.agents.retrieve_agent import RetrieveAgent
from app.agents.reason_agent import ReasonAgent
from app.agents.recommend_agent import RecommendAgent

ingest = IngestAgent()
retrieve = RetrieveAgent()
reason = ReasonAgent()
recommend = RecommendAgent()

def ask(query, patient_id):
    ctx = retrieve.run(query, patient_id)
    answer = reason.run(query, ctx)
    return recommend.run(answer)
