import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_rag_retriever(vector_store):
    if not GROQ_API_KEY:
        # Fallback message for missing key
        def dummy_response(user_input: str, conversation_history=""):
            return "Error: GROQ_API_KEY is missing. Please check your .env file."
        return dummy_response
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
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