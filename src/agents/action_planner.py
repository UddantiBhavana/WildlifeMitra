import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_action_planner_prompt
from dotenv import load_dotenv

load_dotenv()

def get_action_planner():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)   # or 0.4 for planner/reflection
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