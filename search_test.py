from ingest import load_document
from chunking import sentence_based_chunking
from embeddings import embed_chunks
from embeddings import model
from vector_store import build_faiss_index
from sentence_transformers import SentenceTransformer
import numpy as np

text = load_document("sample.docx")

chunks = sentence_based_chunking(text)

chunk_embeddings = embed_chunks(chunks)

index = build_faiss_index(chunk_embeddings)

query = "How Should I Start Learning DSA?"

query_embedding = model.encode([query])

k = 3
distances, indices = index.search(np.array(query_embedding), k)

print("Top Matching Chunks: ")

for idx in indices[0]:
    print(f"Chunk {idx + 1}: {chunks[idx]}")
     