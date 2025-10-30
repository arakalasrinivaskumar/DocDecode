from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from utils.pdf_processor import PDFProcessor
from utils.ocr_engine import OCREngine
import json

app = Flask(__name__)
CORS(app)

# Initialize processors
pdf_processor = PDFProcessor()
ocr_engine = OCREngine()

UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)
    
    try:
        # Process PDF
        result = pdf_processor.process_pdf(filepath)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '')
    
    if not query:
        return jsonify({'error': 'No query provided'}), 400
    
    # Simple text search (replace with vector search in production)
    results = pdf_processor.search_text(query)
    return jsonify({'results': results})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
