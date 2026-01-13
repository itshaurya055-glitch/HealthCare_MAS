from app.pipeline import ask
from app.agents.ingest_agent import IngestAgent

ingest = IngestAgent()

print("🩺 Healthcare Memory Assistant")
print("Type patient info to store, or just press Enter to skip.")
print("Type 'exit' to quit.\n")

PATIENT_ID = "p1"

while True:
    text = input("➕ Add memory (optional): ").strip()
    if text.lower() == "exit":
        break
    if text:
        ingest.run(text, {"patient_id": PATIENT_ID, "type": "note"})
        print("✔ Stored.")

    q = input("❓ Ask a question: ").strip()
    if q.lower() == "exit":
        break
    if q:
        answer = ask(q, PATIENT_ID)
        print("\n🤖 Assistant:")
        print(answer)
        print("-" * 40)
