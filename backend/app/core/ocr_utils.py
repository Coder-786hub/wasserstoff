import pytesseract
from PIL import Image
import fitz
import os

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract_text_from_scanned_pdf(pdf_path):
    text_by_page = ""
    # Open PDF with PyMuPDF
    doc = fitz.open(pdf_path)
    for page in doc:
        # Convert page to image
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        # Extract text using pytesseract
        text = pytesseract.image_to_string(img)
        text_by_page += text
    return text_by_page
