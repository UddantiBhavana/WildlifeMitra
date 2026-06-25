import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_action_planner_prompt
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

def get_action_planner():
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.7,
        groq_api_key=GROQ_API_KEY
    )
    
    def create_action_plan(incident_description: str, rag_context: str = ""):
        system_prompt = get_action_planner_prompt()
        prompt = f"""{system_prompt}

Incident: {incident_description}

Relevant Official Information:
{rag_context}

Create a clear step-by-step action plan:"""
       
        response = llm.invoke(prompt)
        return response.content
   
    return create_action_plan