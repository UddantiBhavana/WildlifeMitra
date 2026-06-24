import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_documents(data_dir="data"):
    """Load all PDFs from data folder"""
    if not os.path.exists(data_dir):
        raise FileNotFoundError(f"Data directory '{data_dir}' not found!")
    
    loader = PyPDFDirectoryLoader(data_dir)
    documents = loader.load()
    
    print(f"✅ Loaded {len(documents)} PDF pages from {data_dir}")
    return documents

def split_documents(documents, chunk_size=1000, chunk_overlap=200):
    """Split documents into chunks"""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    splits = text_splitter.split_documents(documents)
    print(f"✅ Split into {len(splits)} chunks")
    return splits