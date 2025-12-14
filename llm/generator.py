# llm/generator.py

import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load ENV variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Choose the model
MODEL_NAME = "gemini-flash-lite-latest"

def generate_answer(context, question):
    """
    Takes retrieved context and user question,
    and generates an answer using Gemini 1.5 Flash.
    """

    prompt = f"""
    You are an AI assistant using Retrieval-Augmented Generation (RAG).
    Use the context below to answer the user's question.
    If the answer is not in the context, say "Information not available in the documents."

    CONTEXT:
    {context}

    QUESTION:
    {question}

    ANSWER:
    """

    response = genai.GenerativeModel(MODEL_NAME).generate_content(prompt)
    return response.text
