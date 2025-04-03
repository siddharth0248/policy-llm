from app.embeddings import EmbeddingGenerator
from app.database import DatabaseManager

class Chatbot:
    def __init__(self, pdf_directory: str = "/Volumes/D/download_papers/"):
        self.pdf_directory = pdf_directory
        self.texts = utils.extract_text_from_pdfs(self.pdf_directory)
        # Add chunking and embedding generation logic here


    def ask(self, query):
        query_embedding = self.embedding_generator.generate_embeddings([query])[0]
        results = self.db_manager.query_embeddings(query_embedding)
        
        # Combine results into a coherent response (e.g., summarization logic)
        response = "\n".join([res['text'] for res in results])
        return response
