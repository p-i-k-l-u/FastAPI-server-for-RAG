## FastAPI Server for Retrieval-Augmented Generation (RAG)
This FastAPI server is a lightweight Retrieval-Augmented Generation (RAG) solution, allowing ingestion, storage, and querying of documents for embeddings-based retrieval. The server uses ChromaDB as a persistent storage backend and sentence-transformers from Hugging Face for generating document embeddings. It’s optimized for concurrent handling of requests with asynchronous FastAPI endpoints.

# Features
* Document Ingestion and Querying: Supports PDF, DOC, DOCX, and TXT file formats for upload, storage, and querying.
* Embedding Generation: Leverages sentence-transformers/all-MiniLM-L6-v2 from Hugging Face for efficient embeddings.
* ChromaDB Integration: Utilizes ChromaDB for persistent storage and retrieval of embeddings.

# Requirements
* Python 3.12.3
* FastAPI
* Uvicorn
* ChromaDB
* Sentence Transformers (all-MiniLM-L6-v2 model from Hugging Face)

# Setup
https://github.com/p-i-k-l-u/FastAPI-server-for-RAG.git
cd FastAPI-RAG-server

# Install Dependencies:
pip install fastapi uvicorn chromadb sentence-transformers

# Running the Server
uvicorn main:app --host 127.0.0.1 --port 8001
The server will be accessible at http://127.0.0.1:8001 or http://127.0.0.1:8001/docs




