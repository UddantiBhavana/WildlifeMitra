import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()

def get_rag_retriever(vector_store):
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)   # or 0.4 for planner/reflection
    
    def retrieve_and_answer(query: str):
        docs = vector_store.similarity_search(query, k=5)
        context = "\n\n".join([doc.page_content for doc in docs])
        
        prompt = ChatPromptTemplate.from_template(
            """Answer the question based only on the following context:
Context: {context}

Question: {question}

Answer:"""
        )
        chain = prompt | llm
        response = chain.invoke({"context": context, "question": query})
        return response.content, docs  # Return answer + source docs
    
    return retrieve_and_answer