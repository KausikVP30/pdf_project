from ingest import load_document
from chunking import chunk_text

text = load_document("sample.docx")
chunk = chunk_text(text)

print(f"Total Chunks: {len(chunk)}")
print(f"First Chunk: {chunk[0]}")
print(f"Second Chunk: {chunk[1]}")