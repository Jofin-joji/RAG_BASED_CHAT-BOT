📚 RAG Chatbot — FAISS + Gemini 1.5 Flash

A simple, modular Retrieval-Augmented Generation (RAG) chatbot built using Python, FAISS, Sentence Transformers, and Gemini-1.5-Flash.

🚀 Overview

This project demonstrates a beginner-friendly yet powerful RAG (Retrieval-Augmented Generation) chatbot.
It loads your documents, chunks them, embeds them, stores them in a FAISS vector database, retrieves relevant information based on a query, and uses Gemini-1.5-Flash to generate accurate answers.

A simple Streamlit UI is included for an easy interactive chat experience.

✨ Features

🔍 Semantic search using FAISS

🧠 Gemini-1.5-Flash for fast, high-quality LLM responses

📄 ETL pipeline for extracting, transforming, and loading documents

🧩 Fully modular codebase — perfect for learning

💬 Streamlit web UI

⚡ Lightweight and beginner-friendly

🗂️ Project Structure
rag-chatbot/
│
├── data/                       # Raw text files for knowledge base
│     └── sample.txt
│
├── etl/
│     ├── extract.py            # Load raw files
│     ├── transform.py          # Chunk data
│     └── load.py               # ETL pipeline runner
│
├── embeddings/
│     └── embedder.py           # Create text embeddings
│
├── vectorstore/
│     └── faiss_store.py        # FAISS index handling
│
├── llm/
│     └── generator.py          # Gemini response generator
│
├── chatbot/
│     └── rag_chatbot.py        # Complete RAG pipeline
│
├── app.py                      # Streamlit UI
└── main.py                     # Command-line chatbot entry point

🛠️ Installation
1. Create Conda Environment
conda create -n ragbot python=3.10 -y
conda activate ragbot

2. Install Dependencies
pip install faiss-cpu sentence-transformers langchain google-generativeai python-dotenv streamlit

🔑 Setup Your API Key

Create a .env file in the project root:

GEMINI_API_KEY=your_api_key_here

📄 Add Your Documents

Place your .txt files inside the data/ folder.

Example:

data/
└── sample.txt

▶️ Running the Chatbot (Terminal Mode)
python main.py

💻 Running the Web UI (Streamlit)
streamlit run app.py


This launches an interactive browser-based UI.

🧠 How It Works (RAG Pipeline)

Extract → Loads .txt files

Transform → Cleans + chunks text into small pieces

Embed → Converts chunks into vector embeddings

Store → Saves vectors inside a FAISS index

Retrieve → Finds top relevant chunks for a query

Generate → Gemini-1.5-Flash uses retrieved context to answer

🧩 Technologies Used

Python

FAISS — Vector similarity search

Sentence Transformers — Generating embeddings

Gemini 1.5 Flash — Large Language Model

Streamlit — Web UI

dotenv — Environment variable support

