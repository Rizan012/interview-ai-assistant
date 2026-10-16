from io import BytesIO
from pypdf import PdfReader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_experimental.text_splitter import SemanticChunker

from embeddings import embeddings


def clean_text(filename:str,content:str)->str:

    #for .pdf & with multiple pages
    if filename.endswith(".pdf"):
        reader = PdfReader(BytesIO(content))
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    #for .txt 
    if filename.lower().endswith(".txt"):
        return content.decode("utf-8")
    

def recursive_text_chunk(file_content: str) -> list[str]:
    text_splitter= RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    return text_splitter.split_text(file_content)


def semantic_text_chunk(file_content: str) -> list[str]:
    text_splitter = SemanticChunker(
        embeddings,
        buffer_size=0,
        breakpoint_threshold_type="percentile",
        breakpoint_threshold_amount=70,
        min_chunk_size=100,
    )
    return text_splitter.split_text(file_content)

