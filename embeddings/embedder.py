# embeddings/embedder.py

from sentence_transformers import SentenceTransformer

class Embedder:
    """
    Embedding class for converting text into vector embeddings
    using SentenceTransformer.
    """

    def __init__(self, model_name="all-MiniLM-L6-v2"):
        print(f"Loading embedding model: {model_name}")
        self.model = SentenceTransformer(model_name)

    def embed_text(self, text_list):
        """
        Accepts a list of text chunks.
        Returns a list of dense vector embeddings.
        """
        return self.model.encode(text_list, convert_to_numpy=True)
