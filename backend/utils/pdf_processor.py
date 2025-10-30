import PyPDF2
import os
import json
from .ocr_engine import OCREngine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class PDFProcessor:
    def __init__(self):
        self.ocr_engine = OCREngine()
        self.documents = []
        self.vectorizer = TfidfVectorizer(stop_words='english')
        self.tfidf_matrix = None
        
    def process_pdf(self, filepath):
        text_content = []
        tables = []
        images = []
        
        # Try text extraction first
        try:
            with open(filepath, 'rb') as file:
                pdf_reader = PyPDF2.PdfReader(file)
                
                for page_num, page in enumerate(pdf_reader.pages):
                    text = page.extract_text()
                    
                    if text.strip():  # If text extraction worked
                        sections = self._split_into_sections(text, page_num)
                        text_content.extend(sections)
                    else:  # Use OCR for scanned pages
                        ocr_text = self.ocr_engine.extract_text_from_pdf_page(filepath, page_num)
                        sections = self._split_into_sections(ocr_text, page_num)
                        text_content.extend(sections)
                        
        except Exception as e:
            print(f"PDF text extraction failed: {e}")
            # Fallback to OCR
            text = self.ocr_engine.extract_text_from_pdf(filepath)
            sections = self._split_into_sections(text, 0)
            text_content.extend(sections)
        
        # Store in memory (replace with database in production)
        self.documents = text_content
        self._build_search_index()
        
        return {
            'sections': len(text_content),
            'tables': len(tables),
            'images': len(images),
            'status': 'processed'
        }
    
    def _split_into_sections(self, text, page_num):
        # Simple section splitting by paragraphs
        paragraphs = text.split('\n\n')
        sections = []
        
        for i, para in enumerate(paragraphs):
            if len(para.strip()) > 50:  # Minimum length for a section
                sections.append({
                    'id': f'page_{page_num}_section_{i}',
                    'content': para.strip(),
                    'page': page_num,
                    'section': i
                })
        
        return sections
    
    def _build_search_index(self):
        if self.documents:
            texts = [doc['content'] for doc in self.documents]
            self.tfidf_matrix = self.vectorizer.fit_transform(texts)
    
    def search_text(self, query, top_k=5):
        if not self.documents or self.tfidf_matrix is None:
            return []
        
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        
        # Get top matches
        top_indices = np.argsort(similarities)[-top_k:][::-1]
        
        results = []
        for idx in top_indices:
            if similarities[idx] > 0.1:  # Minimum similarity threshold
                doc = self.documents[idx]
                results.append({
                    'content': doc['content'][:200] + '...' if len(doc['content']) > 200 else doc['content'],
                    'page': doc['page'],
                    'score': float(similarities[idx])
                })
        
        return results