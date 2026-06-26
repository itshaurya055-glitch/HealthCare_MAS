from app.pipeline import ask
from app.agents.ingest_agent import IngestAgent

ingest = IngestAgent()

print("=" * 50)
print("🩺 Healthcare Memory Assistant")
print("Store patient notes and ask healthcare-related questions.")
print("Type 'exit' at any prompt to quit.")
print("=" * 50)

PATIENT_ID = "p1"

while True:
    text = input("\n➕ Add memory (optional): ").strip()

    if text.lower() == "exit":
        print("\n👋 Exiting Healthcare Memory Assistant...")
        break

    if text:
        ingest.run(text, {"patient_id": PATIENT_ID, "type": "note"})
        print("✅ Memory stored successfully.")
    else:
        print("ℹ️ No memory added.")

    q = input("\n❓ Ask a question: ").strip()

    if q.lower() == "exit":
        print("\n👋 Exiting Healthcare Memory Assistant...")
        break

    if not q:
        print("⚠️ Please enter a valid question.")
        continue

    answer = ask(q, PATIENT_ID)

    print("\n🤖 Assistant Response")
    print("-" * 50)
    print(answer)
    print("-" * 50)
