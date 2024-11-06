import chromadb

# Initialize ChromaDB client with a persistent directory for storing the documents and embeddings
def initialize_chromadb():
    return chromadb.Client(chromadb.config.Settings(
        persist_directory="./chroma_persist"
    ))
