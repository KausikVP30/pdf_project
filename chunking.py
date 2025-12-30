import re

def chunk_text(text, chunk_size = 500, overlap = 100):
    chunks = []
    start = 0
    text_length = len(text)

    while start < text_length:
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap # to preserve context

    return chunks

def split_into_sentences(text):
    sentences = re.split(r'(?<=[.!?])\s+', text) #regex is extremely strict even spaces break it
    return sentences

def sentence_based_chunking(text, chunk_size = 500, overlap_sentences = 2):

    sentences = split_into_sentences(text)
    
    chunks = []
    current_chunk = []
    current_length = 0

    for sentence in sentences:
        sentence_length = len(sentence)

        if current_length + sentence_length > chunk_size and current_chunk:
            chunks.append(" ".join(current_chunk))

            current_chunk = current_chunk[-overlap_sentences:]
            current_length = sum(len(s) for s in current_chunk) #check

        current_chunk.append(sentence)
        current_length += sentence_length
    
    if current_chunk:
        chunks.append(" ".join(current_chunk))

    return chunks

