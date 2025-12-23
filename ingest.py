from logging import exception
from pypdf import PdfReader
import re # for regex or regular expressions
from docx import Document
import os

def extract_pdf_text(file_path):
    reader = PdfReader(file_path)
    text = ""

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
    
    return text

def extract_txt_text(file_path):
    with open(file_path, "r", encoding="utf-8") as f: # encoding to store the characters as bytes and "utf-8" as it supports and is industry standard
        return f.read()

def extract_docx_text(file_path):
    doc = Document(file_path)
    text = []

    for para in doc.paragraphs:
        if para.text.strip():
            text.append(para.text)
        
    return "\n".join(text) # this basically converts the items in the list as one whole string seperated by a newline

def refining_text(text):
    refined_text = re.sub(r"/s+", " ", text) # reads extra spaces or newlines through (/s+) and replaces by single space to improve chunking
    # r"" means raw string
    # "re" is for pattern based substitution
    return refined_text.strip()
    # strip() removes the leading and ending unwanted whitespaces

def load_document(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == ".pdf":
        text = extract_pdf_text(file_path)
        print(text[:100])

    elif ext == ".txt":
        text = extract_txt_text(file_path)
        print(text[:100])
    
    elif ext == ".docx":
        text = extract_docx_text(file_path)
        print(text[:100])

    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return refining_text(text)


if __name__ == "__main__":
    for file in ["sample2.pdf", "sample.txt", "sample.docx"]:
        try:
            text = load_document(file)
            print(f"{file} -> {len(text)} Characters")
            print("-" * 40)
        except Exception as e:
            print(f"Error in {file}: {e}")


