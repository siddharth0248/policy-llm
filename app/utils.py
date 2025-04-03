from pathlib import Path
from pypdf import PdfReader

def extract_text_from_pdfs(directory: str, limit: int = 10):
    pdf_paths = sorted(Path(directory).glob("*.pdf"))[:limit]
    texts = []
    for pdf_path in pdf_paths:
        reader = PdfReader(pdf_path)
        texts.append({
            "filename": pdf_path.name,
            "content": "".join(page.extract_text() for page in reader.pages)
        })
    return texts
