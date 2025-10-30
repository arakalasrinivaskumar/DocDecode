import pytesseract
from pdf2image import convert_from_path
import os

class OCREngine:
    def __init__(self):
        # Set tesseract path (adjust for your system)
        # pytesseract.pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
        pass
    
    def extract_text_from_pdf(self, pdf_path):
        """Extract text from PDF using OCR"""
        try:
            images = convert_from_path(pdf_path, dpi=200)
            text = ""
            
            for image in images:
                page_text = pytesseract.image_to_string(image)
                text += page_text + "\n\n"
            
            return text
        except Exception as e:
            print(f"OCR failed: {e}")
            return ""
    
    def extract_text_from_pdf_page(self, pdf_path, page_num):
        """Extract text from specific PDF page using OCR"""
        try:
            images = convert_from_path(pdf_path, dpi=200, first_page=page_num+1, last_page=page_num+1)
            if images:
                return pytesseract.image_to_string(images[0])
            return ""
        except Exception as e:
            print(f"OCR for page failed: {e}")
            return ""