import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_prevention_agent_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
def get_prevention_agent():
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
   
    def get_prevention_tips(incident_type: str = "general"):
        system_prompt = get_prevention_agent_prompt()
        prompt = f"""{system_prompt}

Incident Type: {incident_type}

Provide practical prevention and coexistence tips suitable for rural Andhra Pradesh:"""
       
        response = llm.invoke(prompt)
        return response.content
   
    return get_prevention_tips