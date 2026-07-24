from src.ai.client import get_llm

llm = get_llm()

response = llm.invoke(
    "Reply with exactly: Hello from Groq"
)

print(response.content)