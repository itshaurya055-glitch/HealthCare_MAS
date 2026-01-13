from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

class ReasonAgent:
    def run(self, query, context):
        joined = "\n".join(context)
        prompt = f"""
You are a medical assistant.
Use only the information below.
Do not guess.

Context:
{joined}

Question: {query}
"""
        return llm.invoke(prompt).content
