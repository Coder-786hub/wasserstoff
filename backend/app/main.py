from fastapi import FastAPI, UploadFile, File
import os
from app.core.document_parser import extract_text_from_pdf
from app.core.ocr_utils import extract_text_from_scanned_pdf
from app.services.vectorstore_service import add_document_chunks, search
from app.services.gemini_service import run_gemini_prompt
from sentence_transformers import SentenceTransformer
app = FastAPI()

import traceback

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...), ocr: bool = False):
    try:
        contents = await file.read()
        upload_dir = "backend/data/uploaded_docs"
        os.makedirs(upload_dir, exist_ok=True)
        path = os.path.join(upload_dir, file.filename)
        with open(path, "wb") as f:
            f.write(contents)

        if ocr:
            text_pages = extract_text_from_scanned_pdf(path)
        else:
            text_pages = extract_text_from_pdf(path)

        for page in text_pages:
            chunks = page.split("\n\n")
            add_document_chunks(chunks, file.filename)

        return {"status": "uploaded", "chunks_added": len(text_pages)}
    except Exception as e:
        traceback.print_exc()
        return {"error": str(e)}


@app.get("/query/")
def query_documents(query: str):
    chunks = search(query)
    context = "\n".join([c["text"] for c in chunks])
    answer = run_gemini_prompt(query, context)
    return {"answer": answer, "citations": chunks}




