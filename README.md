# Legal Reference Bot

A powerful legal research assistant that combines FastAPI, Gemini Pro AI, and Streamlit to provide instant access to legal precedents, statutes, and case law

## Features

- Instant legal research using Gemini Pro AI
- Clean and intuitive Streamlit interface
- FastAPI backend with CORS support
- Real-time legal summaries and precedents

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory:
```
GEMINI_API_KEY=your_gemini_api_key_here
```

3. Start the FastAPI backend:
```bash
cd backend
uvicorn main:app --reload
```

4. In a new terminal, start the Streamlit frontend:
```bash
cd frontend
streamlit run app.py
```

## Usage

1. Open your browser and navigate to `http://localhost:8501`
2. Enter your legal query in the text input
3. Click "Search" to get instant legal information including:
   - Relevant statutes
   - Case precedents
   - Legal summaries

## Example Queries

- "What are the legal consequences of breach of contract?"
- "Explain the provisions of Section 30 of the Indian Penal Code"
- "What is the legal framework for data protection in India?"
