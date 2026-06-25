import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

import streamlit as st
from dotenv import load_dotenv

# Load .env for local development
load_dotenv()

# Robust API Key handling for Local + Cloud
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    # Fallback for Streamlit Cloud
    try:
        GROQ_API_KEY = st.secrets["GROQ_API_KEY"]
    except:
        GROQ_API_KEY = None

if not GROQ_API_KEY:
    st.error("❌ GROQ_API_KEY is missing!\n\n"
             "→ Local: Add it to your `.env` file\n"
             "→ Streamlit Cloud: Add it in Secrets (TOML format)")
    st.stop()

# Now import the rest
from src.rag_setup import setup_vector_store
from src.agents.intake_agent import get_intake_agent
from src.agents.rag_retriever import get_rag_retriever
from src.agents.action_planner import get_action_planner
from src.agents.prevention_agent import get_prevention_agent
from src.agents.reflection_agent import get_reflection_agent
from src.utils.helpers import format_sources, get_emergency_contacts

st.set_page_config(page_title="WildlifeMitra", page_icon="🦒", layout="wide")

# Professional Styling
st.markdown("""
<style>
    .main-header {font-size: 3rem; color: #1E5631; text-align: center; margin-bottom: 10px;}
    .stButton>button {background-color: #1E5631; color: white; font-weight: bold; border-radius: 8px; height: 52px;}
    .emergency-btn>button {background-color: #C62828; color: white; font-weight: bold; border-radius: 8px; height: 52px;}
</style>
""", unsafe_allow_html=True)

st.markdown('<h1 class="main-header">🐘 WildlifeMitra</h1>', unsafe_allow_html=True)
st.markdown("**Agentic RAG-Powered Human-Wildlife Conflict Mediator for Andhra Pradesh**")

# Initialize
if "messages" not in st.session_state:
    st.session_state.messages = []
if "vector_store" not in st.session_state:
    with st.spinner("Loading official documents & knowledge base..."):
        st.session_state.vector_store = setup_vector_store()

# Sidebar
with st.sidebar:
    st.markdown("<h2 style='text-align: center; color: #1E5631;'>🌿</h2>", unsafe_allow_html=True)
    st.header("About WildlifeMitra")
    st.write("Supporting **SDG 15** (Life on Land) + **SDG 11**")
    st.divider()
    
    st.subheader("🚨 Emergency Contacts")
    if st.button("📞 Show Andhra Pradesh Forest Helplines", type="primary", use_container_width=True):
        st.success(get_emergency_contacts())
    
    st.divider()
    if st.button("🗑️ Clear Conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Report Incident", "🛡️ Prevention Tips", "📖 General Guidance"])

with tab1:
    st.subheader("Report Human-Wildlife Conflict")
    user_input = st.text_area("Describe the incident (English or Telugu allowed):", 
                             height=160, placeholder="Example: ఏనుగు మా పొలంలోకి వచ్చి పంటను నాశనం చేసింది...")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("🚨 Get Help", type="primary", use_container_width=True):
            if user_input.strip():
                with st.spinner("Agents are working..."):
                    intake_agent = get_intake_agent()
                    intake_reply = intake_agent(user_input)
                    
                    st.session_state.messages.append({"role": "user", "content": user_input})
                    st.session_state.messages.append({"role": "assistant", "content": intake_reply})
                    
                    retriever = get_rag_retriever(st.session_state.vector_store)
                    rag_answer, sources = retriever(user_input)
                    
                    planner = get_action_planner()
                    action_plan = planner(user_input, rag_answer)
                    
                    st.success("**Empathy & Initial Response**")
                    st.write(intake_reply)
                    
                    st.subheader("📋 Recommended Action Plan")
                    st.info(action_plan)
                    
                    st.subheader("📚 Official Document Sources")
                    st.write(format_sources(sources))
                    
                    reflection_agent = get_reflection_agent()
                    reflection = reflection_agent(str(st.session_state.messages))
                    st.subheader("🔍 Final Summary & Recommendation")
                    st.write(reflection)
            else:
                st.warning("Please describe the incident.")

    with col2:
        if st.button("🚨 Call Forest Emergency", type="secondary", use_container_width=True):
            st.error("**Immediate Action Required**\n\n" + get_emergency_contacts())

with tab2:
    st.subheader("🛡️ Prevention & Coexistence Tips")
    st.caption("💡 You can use this tab anytime for general prevention advice")
    incident_type = st.selectbox("Select type of conflict", 
                                ["Elephant", "Leopard", "Wild Boar", "Monkey", "General"])
    
    if st.button("Get Practical Tips", use_container_width=True):
        with st.spinner("Fetching best practices..."):
            prevention_agent = get_prevention_agent()
            tips = prevention_agent(incident_type)
            st.write(tips)

with tab3:
    st.subheader("📖 General Guidance & Resources")
    st.info("**For informational purposes only.** Always contact your local Forest Department for official action.")
    st.write("**State Wildlife Helpline:** **1926**")

# Conversation History
st.divider()
st.subheader("Conversation History")
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

st.caption("WildlifeMitra v1.0 | Built for 1M1B AI for Sustainability Internship")