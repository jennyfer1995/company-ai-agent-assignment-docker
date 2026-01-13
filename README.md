# Company AI Agent – Agentic RAG System

This project is an **Agentic AI system** built as part of a **technical assessment**.  
It answers company internal policy questions by intelligently deciding whether to:
- Answer directly using an LLM, or
- Retrieve information from internal documents using **Retrieval-Augmented Generation (RAG)**.

## 🎯 Assessment Tasks Covered

### ✅ Task 1: AI Agent Development
- Accepts user queries
- Decides between **LLM response** or **Document retrieval**
- Uses **prompt engineering**
- Implements **tool calling**
- Maintains **session-based memory**

### ✅ Task 2: Retrieval-Augmented Generation (RAG)
- Sample internal policy documents provided
- Documents converted to embeddings
- Embeddings stored using **FAISS**
- Relevant document chunks retrieved
- Context passed to the LLM

### ✅ Task 3: Backend API
- Built using **FastAPI**
- Exposes `/ask` endpoint
- Returns structured response with sources

### ✅ Task 4: Azure-Ready Deployment
- Dockerized application
- Environment-based secrets
- Designed for **Azure App Service / Azure Functions**
- Compatible with **Azure OpenAI**
- Basic logging enabled

### ✅ Task 5: Documentation
- Complete README with setup, architecture, and design decisions

---

## 🚀 Key Features

- Agent-based query routing (LLM vs RAG)
- FAISS vector store for fast retrieval
- Session-based conversational memory
- REST API with Swagger UI
- Docker containerization
- Azure OpenAI compatible design

---
<img width="1552" height="868" alt="image" src="https://github.com/user-attachments/assets/b0c76f02-099c-4410-9687-e2ad924f8916" />

<img width="1868" height="812" alt="image" src="https://github.com/user-attachments/assets/0b3a3e9e-b5a4-437d-8f2e-82c231e1034c" />


---

## 🧠 High-Level Architecture
User Query
↓
Agent Router
↓
┌───────────────┐
│ Policy Query? │── Yes ──→ Retrieve Documents → LLM + Context
└───────────────┘
│
No
↓
Direct LLM Answer
↓
Structured Response + Sources


## 🛠 Tech Stack

- **Language:** Python 3.11
- **Backend:** FastAPI
- **Vector Store:** FAISS
- **LLM:** OpenAI / Azure OpenAI
- **Containerization:** Docker
- **Version Control:** Git + GitHub

---

## 📂 Project Structure

## ▶️ Run Locally (Without Docker)

### 1️⃣ Install dependencies
```bash
pip install -r requirements.txt
**#Set environment variable**
export OPENAI_API_KEY=your_api_key
**#Start the API**
uvicorn app.api:app --reload
**#Open Swagger UI**
http://localhost:8000/docs

## ▶️ Run with Docker
1️⃣ Build image
docker build -t company-ai-agent .

2️⃣ Run container
docker run -p 8000:8000 \
  -e OPENAI_API_KEY=your_api_key \
  company-ai-agent

3️⃣ Access API
http://localhost:8000/docs



