import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_reflection_agent_prompt
from dotenv import load_dotenv

load_dotenv()

def get_reflection_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.5)   # or 0.4 for planner/reflection
    
    def reflect_and_escalate(full_conversation: str):
        system_prompt = get_reflection_agent_prompt()
        prompt = f"""{system_prompt}

Full Conversation:
{full_conversation}

Provide a final summary, key actions, and decide if escalation to authorities is recommended:"""
        
        response = llm.invoke(prompt)
        return response.content
    
    return reflect_and_escalate