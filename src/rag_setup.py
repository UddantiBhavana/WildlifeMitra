import sys
import os

# Add project root to Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.utils.document_loader import load_documents, split_documents
from src.utils.embeddings import get_embeddings
from langchain_community.vectorstores import FAISS

def setup_vector_store(index_path="vector_store/faiss_index"):
    """Create or load FAISS vector store"""
    os.makedirs("vector_store", exist_ok=True)
    
    embeddings = get_embeddings()
    
    index_file = f"{index_path}.faiss"
    if os.path.exists(index_file) and os.path.exists(f"{index_path}.pkl"):
        print("✅ Loading existing FAISS index...")
        vector_store = FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)
    else:
        print("📄 Loading PDFs and creating new FAISS index...")
        documents = load_documents()
        splits = split_documents(documents)
        
        vector_store = FAISS.from_documents(splits, embeddings)
        vector_store.save_local(index_path)
        print(f"✅ FAISS vector store created and saved!")
    
    return vector_store

# Test
if __name__ == "__main__":
    vector_store = setup_vector_store()
    print("✅ Vector store is ready!")

