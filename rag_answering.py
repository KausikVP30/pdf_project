import os
from openai import OpenAI

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY_PDF_PROJECT"))

def generate_rag_answer(retrieved_chunks, query):
    context = "\n\n".join(retrieved_chunks)

    prompt = f"""

You are a question answering system.

RULES:
1. Use ONLY the information in the context.
2. Do NOT use outside knowledge.
3. If the answer is not present, say exactly:
    "I could not find the answer in the provided document."
4. Be concise and factual.

CONTEXT:
{context}

Query:
{query}

FINAL ANSWER:
"""

    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        messages = [
            {"role": "user", "content": prompt}
        ],
        temperature = 0,
        max_tokens = 200
    )

    return response.choices[0].message.content.strip() 