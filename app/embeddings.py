from langchain.embeddings import LlamaEmbeddings

class EmbeddingGenerator:
    def __init__(self):
        self.model = LlamaEmbeddings()

    def generate_embeddings(self, text_chunks):
        return [self.model.embed(chunk) for chunk in text_chunks]
