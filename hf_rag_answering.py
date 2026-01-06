import os
import requests

HF_API_TOKEN = os.getenv("HF_API_TOKEN")
HF_MODEL = "google/gemma-2-2b-it"
HF_URL = f"https://api-inference.huggingface.co/models/{HF_MODEL}"

HEADERS = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}

def generate_rag_answer(retrieved_chunks, query):

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
{query}

ANSWER:
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 200,
            "temperature": 0.1,
            "top_p": 0.9,
            "return_full_text": False
        }
    }

    response = requests.post(HF_URL, headers = HEADERS, json = payload)
    response.raise_for_status()

    return response.json()[0]("generated_text").strip()