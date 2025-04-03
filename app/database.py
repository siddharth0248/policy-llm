import chromadb

class DatabaseManager:
    def __init__(self):
        self.db = chromadb.Client()
        self.collection = self.db.get_or_create_collection(name="pdf_embeddings")

    def store_embeddings(self, embeddings, metadata):
        for i, (embedding, meta) in enumerate(zip(embeddings, metadata)):
            self.collection.add(
                ids=[f"doc_{i}_chunk_{j}" for j in range(len(embedding))],
                embeddings=embedding,
                metadatas=meta
            )

    def query_embeddings(self, query_embedding):
        results = self.collection.query(query_embedding, n_results=3)
        return results
