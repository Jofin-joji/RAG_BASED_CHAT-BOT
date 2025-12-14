# vectorstore/faiss_store.py

import faiss
import numpy as np

class FaissVectorStore:
    """
    Simple FAISS vector store for storing and retrieving embeddings.
    """

    def __init__(self, embedding_dim):
        # Create a FAISS index for cosine similarity (inner product)
        self.index = faiss.IndexFlatIP(embedding_dim)
        self.text_chunks = []   # store text
        self.embeddings = []    # store embeddings

    def add_documents(self, chunks, vectors):
        """
        Add text chunks + their embeddings to FAISS.
        """
        vectors = np.array(vectors).astype("float32")

        # Normalize vectors for cosine similarity
        faiss.normalize_L2(vectors)

        self.index.add(vectors)
        self.embeddings.extend(vectors)
        self.text_chunks.extend(chunks)

    def search(self, query_vector, top_k=3):
        """
        Search FAISS for the top_k similar documents.
        """
        query_vector = np.array([query_vector]).astype("float32")
        faiss.normalize_L2(query_vector)

        distances, indices = self.index.search(query_vector, top_k)

        # Retrieve text chunks
        results = []
        for idx in indices[0]:
            results.append(self.text_chunks[idx])

        return results
