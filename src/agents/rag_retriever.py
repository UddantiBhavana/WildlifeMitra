import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

def get_rag_retriever(vector_store):
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.3,
        groq_api_key=GROQ_API_KEY
    )
   
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
        return response.content, docs
   
    return retrieve_and_answer