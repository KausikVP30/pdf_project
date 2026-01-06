from ingest import load_document
from chunking import sentence_based_chunking
from embeddings import embed_chunks
from vector_store import build_faiss_index
from local_rag_answering import generate_rag_answer
from sentence_transformers import SentenceTransformer
import numpy as np


text = load_document("sample.docx")

chunks = sentence_based_chunking(text)

chunk_embeddings = embed_chunks(chunks)

index = build_faiss_index(chunk_embeddings)

query = "How should I start learning DSA?"
model = SentenceTransformer("all-MiniLM-L6-v2")
query_embedding = model.encode([query])

k = 2
_, indices = index.search(np.array(query_embedding), k)
retrieved_chunks = [chunks[i] for i in indices[0]]

answer = generate_rag_answer(retrieved_chunks, query)

print("\nANSWER:\n")
print(answer)
