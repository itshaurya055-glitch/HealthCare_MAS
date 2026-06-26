from app.pipeline import ask
from app.agents.ingest_agent import IngestAgent

ingest = IngestAgent()

print("🩺 Healthcare Memory Assistant")
print("Patient ID:", "p1")
print("Commands:")
print("  - Type patient information to store it")
print("  - Press Enter to skip memory storage")
print("  - Type 'exit' anytime to quit\n")

PATIENT_ID = "p1"

while True:
    text = input("➕ Add memory (optional): ").strip()

    if text.lower() == "exit":
        print("👋 Session ended.")
        break

    if text:
        print("📥 Saving patient memory...")
        ingest.run(text, {"patient_id": PATIENT_ID, "type": "note"})
        print("✅ Memory saved successfully.")

    q = input("❓ Ask a question: ").strip()

    if q.lower() == "exit":
        print("👋 Session ended.")
        break

    if not q:
        print("⚠️ Please enter a question.\n")
        continue

    print("🤖 Thinking...\n")

    answer = ask(q, PATIENT_ID)

    print("=" * 50)
    print("🤖 Assistant")
    print("=" * 50)
    print(answer)
    print("=" * 50)
