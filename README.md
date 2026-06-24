# 🐘 WildlifeMitra

**Agentic RAG-Powered Human-Wildlife Conflict Mediator for Andhra Pradesh**

An intelligent multi-agent system designed to help farmers and villagers in Andhra Pradesh resolve human-wildlife conflicts using official government documents and practical guidance.

## 🎯 Project Highlights

* **Multi-Agent Architecture** with 5 specialized agents
* **RAG** over official PDFs (Project HANUMAN, AP Compensation GO, National Guidelines, etc.)
* Bilingual support (English + Telugu)
* Actionable plans, prevention tips, and escalation recommendations
* Source citations for transparency

## 🛠️ Tech Stack

* **Backend**: Python, LangChain, FAISS, Groq (Llama-3.3)
* **Frontend**: Streamlit
* **Embeddings**: sentence-transformers

## 🌍 Impact

Supports **SDG 15** (Life on Land) and **SDG 11** (Sustainable Cities and Communities) by promoting peaceful human-wildlife coexistence.

---

## 🚀 Quick Setup

1. Clone / Open the project folder

2. Create virtual environment:

```cmd
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```cmd
pip install -r requirements.txt
```

4. Add your Groq API key in `.env` file

5. Place all PDFs in the `data/` folder

6. Run the app:

```cmd
streamlit run streamlit_app.py
```

## 📁 Project Structure

```text
WildlifeMitra/
├── data/                    # Official PDFs
├── vector_store/            # FAISS index
├── src/
│   ├── agents/              # 5 specialized agents
│   ├── prompts/
│   ├── utils/
│   └── rag_setup.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── responsible_ai.md
```

## ✨ Key Features

* Report Incident with empathetic AI response
* Personalized Action Plans
* Prevention & Coexistence Tips
* Emergency Forest Helplines
* Official Document Citations

**Built as part of 1M1B AI for Sustainability Internship**
