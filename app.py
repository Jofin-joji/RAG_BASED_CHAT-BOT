import streamlit as st
from etl.load import prepare_documents
from chatbot.rag_chatbot import RAGChatbot

# --------------------------
# SIMPLE STREAMLIT UI FOR RAG CHATBOT
# --------------------------

st.set_page_config(page_title="RAG Chatbot", layout="wide")
st.title("📚 RAG Chatbot — FAISS + Gemini UI")

@st.cache_resource

def load_chatbot():
    documents = prepare_documents("data")
    chatbot = RAGChatbot(documents)
    return chatbot

chatbot = load_chatbot()

st.write("Ask any question based on your uploaded documents.")

user_query = st.text_input("Your Question", placeholder="Type your question here...")

if st.button("Ask"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating answer..."):
            response = chatbot.ask(user_query)
        st.subheader("Answer:")
        st.write(response)

st.markdown("---")
st.caption("Simple UI built with Streamlit")
