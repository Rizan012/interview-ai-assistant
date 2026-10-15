from pypdf import PdfReader
from pathlib import Path

def extract_text(file_path):
    path = Path(r"C:\Users\cesst\Documents\ReeDoc\rizan_shrestha_resume.pdf")

    if path.suffix.lower() == ".pdf":
        reader = PdfReader(path)
        return "\n".join(page.extract_text() or "" for page in reader.pages)

    if path.suffix.lower() == ".txt":
        return path.read_text(encoding="utf-8")

    raise ValueError("Only PDF and TXT files are supported.")

print(extract_text("info.txt"))