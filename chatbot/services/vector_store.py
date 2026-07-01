import chromadb


class VectorStore:
    client = chromadb.PersistentClient(path="./chroma_db")

    collection = client.get_or_create_collection(
        name="document_chunks"
    )

    @classmethod
    def add_chunk(cls, chunk_id, text, embedding, metadata=None):
        cls.collection.add(
            ids=[str(chunk_id)],
            documents=[text],
            embeddings=[embedding],
            metadatas=[metadata or {}],
        )

    @classmethod
    def search(cls, embedding, top_k=5):
        results = cls.collection.query(
            query_embeddings=[embedding],
            n_results=top_k,
        )
        return results