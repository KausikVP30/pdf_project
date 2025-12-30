from ingest import load_document
from chunking import sentence_based_chunking

text = load_document("sample.docx")
chunks = sentence_based_chunking(text)

for i,chunk in enumerate(chunks[:3]):
    print(f"Chunk {i}: {chunk}")