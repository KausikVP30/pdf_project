import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "deepseek-r1:8b"

def generate_rag_answer(question, retrieved_chunks):
    """
    Generate an answer using a local Ollama model (DeepSeek R1 8B).
    """
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""
You are a document question answering system.

RULES:
1. Use ONLY the information in the context.
2. Do NOT use outside knowledge.
3. If the answer is not present, say exactly:
    "I could not find the answer in the provided document."
4. Be concise and factual.

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False,
        "options": {
            "temperature": 0.1,
            "num_predict": 300
        }
    }

    response = requests.post(OLLAMA_URL, json=payload)
    response.raise_for_status()

    return response.json()["response"].strip()
