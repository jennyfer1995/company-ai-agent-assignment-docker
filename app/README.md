Company AI Agent – Agentic RAG System
📌 Project Overview

This project implements an Agentic AI system that can intelligently answer user queries by either:

Responding directly using a Large Language Model (LLM), or

Retrieving relevant information from internal company documents using Retrieval-Augmented Generation (RAG).

The system is designed as a backend service using FastAPI, supports session-based memory, and is deployment-ready for Azure App Service with Azure OpenAI.

🧠 Architecture Overview

High-level flow:

User sends a query to /ask API

Agent decides:

LLM route → direct answer

TOOL route → retrieve relevant documents

Retrieved context is injected into the response

Session memory is updated

Structured response is returned

Client → FastAPI → Agent Router
                  ├── LLM (Azure OpenAI)
                  └── RAG (FAISS + Documents)

🛠 Tech Stack Used

Language: Python 3.11

Backend Framework: FastAPI

LLM: Azure OpenAI (design-level integration)

RAG Vector Store: FAISS

Embeddings: OpenAI-compatible embeddings

Containerization: Docker

Deployment Target: Azure App Service

Logging: Python logging module

✅ Task-wise Implementation
🔹 Task 1: AI Agent Development (Core)

Features implemented:

Accepts user query

Intelligent routing:

LLM for general queries

TOOL (RAG) for policy-related queries

Prompt engineering for structured answers

Tool calling for document retrieval

Session-based memory support

Example routing logic:

Keywords like policy, hr, leave, security → TOOL

Other queries → LLM

🔹 Task 2: Retrieval-Augmented Generation (RAG)

Documents Used (sample):

zero500_hr_policy.txt

zero500_it_policy.txt

RAG Pipeline:

Documents loaded and chunked

Converted to embeddings

Stored in FAISS vector index

Relevant chunks retrieved for a query

Context passed to the agent for answering

This ensures answers are grounded in internal documents.

🔹 Task 3: Backend API (FastAPI)
API Endpoint

POST /ask

Request Body:

{
  "query": "string",
  "session_id": "optional"
}


Response:

{
  "answer": "string",
  "route": "LLM | TOOL",
  "sources": ["doc1.txt", "doc2.txt"]
}


The API is fully testable via Swagger UI:

http://localhost:8000/docs

🔹 Task 4: Azure Deployment (Mandatory)
Azure Design Choice

Compute: Azure App Service (Linux)

LLM: Azure OpenAI

Secrets: Environment Variables

Container: Docker

Environment Variables Used

AZURE_OPENAI_API_KEY

AZURE_OPENAI_ENDPOINT

AZURE_OPENAI_DEPLOYMENT_NAME

Docker Support (Bonus ✔)

A Dockerfile is provided to containerize the application.
The application was successfully built and run locally using Docker.

Logging (Bonus ✔)

Basic logging is implemented using Python’s logging module, compatible with Azure Monitor.

Deployment Status

Due to the absence of an active Azure subscription and Azure OpenAI access at submission time, the application was not deployed to a live Azure App Service.

However:

The codebase is fully Azure-ready

All environment variable configurations are in place

Deployment steps are documented

The Docker container can be directly deployed to Azure App Service once access is available

🚀 Local Setup Instructions
1️⃣ Clone the repository
git clone <repo-url>
cd company-ai-agent

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run locally
uvicorn app.api:app --reload

4️⃣ Run using Docker
docker build -t company-ai-agent .
docker run -p 8000:8000 -e OPENAI_API_KEY=dummy_key -e AZURE_OPENAI_DEPLOYMENT_NAME=dummy company-ai-agent

🧪 Example Test (Swagger)
{
  "query": "What is Zero500 hr policy?",
  "session_id": "demo"
}

📌 Design Decisions

Agent-based routing improves efficiency and accuracy

RAG ensures answers are grounded in internal documents

FAISS chosen for simplicity and local testing

Docker ensures cloud portability

Azure App Service selected for scalability and ease of deployment

⚠️ Limitations

Azure OpenAI access not available at submission time

Limited sample documents

Simple keyword-based routing (can be improved)

🔮 Future Improvements

Semantic routing instead of keyword-based routing

Chunk-level citation in responses

Azure AI Search integration

Authentication & role-based access

UI frontend

✅ Final Status

✔ Task 1 – Completed
✔ Task 2 – Completed
✔ Task 3 – Completed
✔ Task 4 – Completed (design + Docker + logging)
✔ Task 5 – Completed