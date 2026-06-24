import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_prevention_agent_prompt
from dotenv import load_dotenv

load_dotenv()

def get_prevention_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)   # or 0.4 for planner/reflection
    
    def get_prevention_tips(incident_type: str = "general"):
        system_prompt = get_prevention_agent_prompt()
        prompt = f"""{system_prompt}

Incident Type: {incident_type}

Provide practical prevention and coexistence tips suitable for rural Andhra Pradesh:"""
        
        response = llm.invoke(prompt)
        return response.content
    
    return get_prevention_tips