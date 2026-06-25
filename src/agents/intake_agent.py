import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_intake_agent_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_intake_agent():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        groq_api_key=GROQ_API_KEY
    )
    
    def intake_response(user_input: str, conversation_history=""):
        system_prompt = get_intake_agent_prompt()
        prompt = f"""{system_prompt}
User Input: {user_input}
Respond empathetically but practically. Use simple Telugu + English."""
        response = llm.invoke(prompt)
        return response.content
    return intake_response