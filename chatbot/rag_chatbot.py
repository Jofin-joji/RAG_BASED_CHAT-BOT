# chatbot/rag_chatbot.py

from embeddings.embedder import Embedder
from vectorstore.faiss_store import FaissVectorStore
from llm.generator import generate_answer

class RAGChatbot:
    """
    Main RAG chatbot class that performs:
    - Embedding search
    - FAISS retrieval
    - Gemini-based answer generation
    """

    def __init__(self, documents):
        # 1. Load embedder
        self.embedder = Embedder()

        # 2. Create FAISS index with correct dimensions
        sample_vec = self.embedder.embed_text(["hello"])[0]
        vector_dim = len(sample_vec)
        self.vector_db = FaissVectorStore(vector_dim)

        # 3. Embed all documents & add to FAISS
        doc_vectors = self.embedder.embed_text(documents)
        self.vector_db.add_documents(documents, doc_vectors)

    def ask(self, query):
        """
        Takes a user query → performs RAG → returns Gemini answer.
        """

        # Embed query
        query_vector = self.embedder.embed_text([query])[0]

        # Retrieve top matching chunks
        retrieved_chunks = self.vector_db.search(query_vector, top_k=3)

        # Combine context
        context = "\n\n".join(retrieved_chunks)

        # Generate response using Gemini-1.5-Flash
        answer = generate_answer(context, query)
        return answer
