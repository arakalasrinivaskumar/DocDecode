const API_BASE = 'http://localhost:5000';

async function uploadPDF() {
    const fileInput = document.getElementById('pdfFile');
    const statusDiv = document.getElementById('uploadStatus');
    
    if (!fileInput.files[0]) {
        showStatus('Please select a PDF file', 'error');
        return;
    }

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    try {
        showStatus('Uploading and processing PDF...', 'info');
        
        const response = await fetch(`${API_BASE}/upload`, {
            method: 'POST',
            body: formData
        });

        const result = await response.json();
        
        if (response.ok) {
            showStatus(`Success! Processed ${result.sections} sections`, 'success');
        } else {
            showStatus(`Error: ${result.error}`, 'error');
        }
    } catch (error) {
        showStatus(`Upload failed: ${error.message}`, 'error');
    }
}

async function searchDocuments() {
    const query = document.getElementById('searchQuery').value;
    const resultsDiv = document.getElementById('searchResults');

    if (!query.trim()) {
        resultsDiv.innerHTML = '<div class="status-error">Please enter a search query</div>';
        return;
    }

    try {
        const response = await fetch(`${API_BASE}/search`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ query: query })
        });

        const result = await response.json();
        
        if (response.ok) {
            displayResults(result.results);
        } else {
            resultsDiv.innerHTML = `<div class="status-error">Error: ${result.error}</div>`;
        }
    } catch (error) {
        resultsDiv.innerHTML = `<div class="status-error">Search failed: ${error.message}</div>`;
    }
}

function displayResults(results) {
    const resultsDiv = document.getElementById('searchResults');
    
    if (results.length === 0) {
        resultsDiv.innerHTML = '<div class="status-info">No results found</div>';
        return;
    }

    resultsDiv.innerHTML = results.map(result => `
        <div class="result-item">
            <div class="result-score">Score: ${result.score.toFixed(3)}</div>
            <div class="result-content">${result.content}</div>
            <div class="result-page">Page: ${result.page + 1}</div>
        </div>
    `).join('');
}

function showStatus(message, type) {
    const statusDiv = document.getElementById('uploadStatus');
    statusDiv.innerHTML = `<div class="status-${type}">${message}</div>`;
}

// Check backend health on load
async function checkHealth() {
    try {
        await fetch(`${API_BASE}/health`);
        console.log('Backend is healthy');
    } catch (error) {
        console.error('Backend is not responding');
    }
}

// Initialize
checkHealth();