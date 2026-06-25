import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_reflection_agent_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def get_reflection_agent():
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
    def reflect_and_escalate(full_conversation: str):
        system_prompt = get_reflection_agent_prompt()
        prompt = f"""{system_prompt}

Full Conversation:
{full_conversation}

Provide a final summary, key actions, and decide if escalation to authorities is recommended:"""
       
        response = llm.invoke(prompt)
        return response.content
   
    return reflect_and_escalate