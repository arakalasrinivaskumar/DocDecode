DocDecode — Intelligent PDF Search Tool

🎓 Course Project
This project was developed by P. Sanjay Krishna, A. Srinivas Kumar, Ayush Mohanty, as part of the **Intel Unnati - AI Program** at **Marri Laxman Reddy Institute of Technology and Management** guided by Mr. V. Naresh Kumar Reddy. The aim was to bridge the gap between document storage and knowledge retrieval, making large PDF datasets easily searchable.

🧠 Introduction

DocDecode is an AI-driven PDF Search and Analysis Tool that converts static PDF files into searchable, structured knowledge.
The system extracts text from both digital and scanned PDFs using OCR (Optical Character Recognition), and enables intelligent semantic search powered by TF-IDF and cosine similarity.

This project bridges the gap between document storage and knowledge retrieval, making large PDF datasets easily searchable and interpretable through a modern web interface.

🎯 Objectives

Extract and analyze content from PDFs (including scanned documents).

Use OCR to process non-selectable text from image-based PDFs.

Build a searchable knowledge base using TF-IDF vectorization.

Provide an intuitive frontend for uploading PDFs and performing keyword searches.

Deliver a foundation for future integration with AI-based vector search and semantic retrieval.

⚙️ Technologies Used
Backend

Flask — lightweight Python web framework

PyPDF2 — PDF text extraction

pytesseract — OCR for image-based PDFs

pdf2image — PDF to image conversion for OCR

scikit-learn — TF-IDF vectorization and cosine similarity

NumPy — numerical computations

Flask-CORS — enables frontend-backend communication

Frontend

HTML5 / CSS3 / JavaScript (ES6)

Responsive UI with a clean, modern design

Fetch API for asynchronous requests

🧩 Backend Overview
🔹 app.py

Flask backend that provides APIs for:

Uploading and processing PDFs (/upload)

Searching processed documents (/search)

Checking server health (/health)

🔹 pdf_processor.py

Handles:

Text extraction from PDFs

OCR fallback for scanned pages

Splitting text into meaningful sections

Building TF-IDF vector representations for search

🔹 ocr_engine.py

Encapsulates all OCR logic using pytesseract and pdf2image to extract text from scanned PDF pages.

💻 Frontend Overview

The web interface allows users to:

Upload and process PDF files.

Search for keywords across all extracted text.

View ranked results with similarity scores and page numbers.

UI Features:

Gradient-based design

Real-time status updates (uploading, success, errors)

Search results with contextual excerpts

🧠 Workflow

User uploads a PDF → sent to Flask backend.

Backend processes the PDF:

Extracts text using PyPDF2

Applies OCR if text extraction fails

Segments content into searchable chunks

TF-IDF Vectorizer builds a document-term matrix.

User performs search → cosine similarity ranks the most relevant text segments.

Frontend displays top results with relevance scores and page references.

🧰 Installation & Setup
🔹 Prerequisites

Python 3.8+

Node.js (optional, for frontend live server)

Tesseract OCR installed on your system

🔹 Backend Setup
cd backend
python -m venv env
source env/bin/activate   # On Windows use: env\Scripts\activate
pip install -r requirements.txt
python app.py


Backend runs by default at:
👉 http://localhost:5000

🔹 Frontend Setup

Simply open frontend/index.html in your browser.
(Or use an extension like Live Server in VS Code for automatic reloads.)

📡 API Endpoints
Endpoint	Method	Description
/upload	POST	Uploads a PDF file for processing
/search	POST	Searches extracted text for a given query
/health	GET	Health check endpoint
📊 Future Enhancements

🧩 Vector Database Integration (e.g., Pinecone, FAISS)

🧠 Transformer-based Search (Sentence-BERT or OpenAI Embeddings)

🗃️ MongoDB Storage for document persistence

💬 Keyword Highlighting in search results

🌐 User Authentication for multi-user environments

🏁 Conclusion

DocDecode transforms static, complex PDF documents into a searchable, explorable, and interpretable knowledge space.
By combining text extraction, OCR, and intelligent search, it bridges the gap between raw data and actionable information — empowering users to discover insights effortlessly.

This project serves as a strong foundation for advanced document intelligence systems powered by AI and Explainable Search.
🏫 Acknowledgment

This project was developed as part of an academic initiative focusing on practical applications of AI and OCR in information retrieval systems.
We extend our gratitude to our mentors and peers for their support throughout this project.
