import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_path):
    try:
        text_by_page = []
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text_by_page.append(page.get_text())
        return text_by_page
    except Exception as e:
        print(f"Error extracting text: {e}")
        return []
