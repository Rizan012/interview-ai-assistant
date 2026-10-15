from io import BytesIO
from pypdf import PdfReader
from langchain_text_splitters import (
    RecursiveCharacterTextSplitter,
    CharacterTextSplitter,
)


def clean_text(filename:str,content:str):

    #for .pdf, accepts multiple pages
    if filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    #for .txt 
    if filename.lower().endswith(".txt"):
        return content.decode("utf-8")
    
