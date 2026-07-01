from sentence_transformers import SentenceTransformer


class EmbeddingService:
    # Load model once when the application starts
    model = SentenceTransformer("all-MiniLM-L6-v2")

    @classmethod
    def generate_embedding(cls, text: str):
        """
        Generate embedding for a single text chunk.
        Returns a list of floats.
        """
        embedding = cls.model.encode(text)
        return embedding.tolist()

    @classmethod
    def generate_embeddings(cls, texts: list[str]):
        """
        Generate embeddings for multiple chunks.
        """
        embeddings = cls.model.encode(texts)
        return embeddings.tolist()