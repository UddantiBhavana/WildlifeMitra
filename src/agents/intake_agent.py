import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from langchain_groq import ChatGroq
from src.prompts.system_prompts import get_intake_agent_prompt
from dotenv import load_dotenv

load_dotenv()

def get_intake_agent():
    llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0.6)
    
    def intake_response(user_input: str, conversation_history=""):
        system_prompt = get_intake_agent_prompt()
        
        prompt = f"""{system_prompt}

User Input: {user_input}

Previous messages: {conversation_history[-500:]}  # Limit history to avoid repetition

Respond empathetically but practically. Use simple Telugu + English. 
Give immediate useful advice. Do not repeat previous responses."""

        response = llm.invoke(prompt)
        return response.content
    
    return intake_response