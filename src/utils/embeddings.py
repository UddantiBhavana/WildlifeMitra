from langchain_huggingface import HuggingFaceEmbeddings

def get_embeddings():
    """Return embedding model"""
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2",
        model_kwargs={'device': 'cpu'}
    )
    return embeddings