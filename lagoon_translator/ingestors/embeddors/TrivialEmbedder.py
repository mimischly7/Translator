from lagoon_translator.ingestors.embeddors.Embedder import Embedder
from numpy.random import randint
from transformers import pipeline
import numpy as np

class TrivialEmbedder(Embedder):
    def __init__(self):
        name = "trivial-embedder"
        dim = 768
        super(TrivialEmbedder, self).__init__(name, dim)

    def embed(self, text):
        embedding_pipeline = pipeline("feature-extraction")
        embeddings = embedding_pipeline(text[:400])
        embeddings = np.array(embeddings)
        # Mean pooling to get a single embedding for the sentence
        sentence_embedding = np.mean(embeddings, axis=1)[0]
        return sentence_embedding
