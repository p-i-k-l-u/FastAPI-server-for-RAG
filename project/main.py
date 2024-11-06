from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from document_processing import extract_text_from_pdf, extract_text_from_docx, extract_text_from_txt
from models import DocumentRequest
from sentence_transformers import SentenceTransformer
import chromadb

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": " FastAPI server for RAG"}
# class Document(BaseModel):
#     filename: str
#     content: str
# ----------------------------------------------------------------------------
# @app.get("/upload_document/")
# async def upload_document(file: UploadFile = File(...)):
#     content = await file.read()
#     filename = file.filename
#     return {"filename": filename, "content": content.decode("utf-8")}

# -------------------------------------------------------------------------------

# Initialize ChromaDB client with a persistent directory for storing the documents and embeddings
client = chromadb.Client(chromadb.config.Settings(
    persist_directory="./chroma_persist"
))

# Load the pre-trained sentence-transformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

@app.post("/upload/")
async def upload_document(file: UploadFile = File(...)):
    try:
        # Read file content based on type
        if file.filename.endswith('.pdf'):
            content = extract_text_from_pdf(file.file)
        elif file.filename.endswith('.docx'):
            content = extract_text_from_docx(file.file)
        elif file.filename.endswith('.txt'):
            content = extract_text_from_txt(file.file)
        else:
            raise HTTPException(status_code=400, detail="Unsupported file type")
        
        # Generate embeddings for the document
        embeddings = model.encode([content])

        # Save embeddings and document content to ChromaDB
        collection = client.get_or_create_collection("documents")
        collection.add(
            documents=[content],
            metadatas=[{"name": file.filename}],
            embeddings=embeddings
        )
        
        return {"message": "Document uploaded successfully", "document_name": file.filename}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/query/")
async def query_documents(query: str):
    try:
        # Generate embeddings for the query
        query_embedding = model.encode([query])

        # Retrieve the most relevant documents from ChromaDB
        collection = client.get_or_create_collection("documents")
        results = collection.query(
            query_embeddings=query_embedding,
            n_results=3  # return top 3 results
        )

        # Return the relevant documents
        return {"query": query, "results": results['documents']}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
