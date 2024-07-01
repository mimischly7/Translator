import torch
from pprint import pprint
from transformers import AutoTokenizer, AutoModel, pipeline
import numpy as np

classifier = pipeline("feature-extraction")
embeddings = classifier("This is customer/client name **Aafiyat Medical Centre** and id 126, located in Mississauga. Th")
# Convert to numpy array for easier manipulation
embeddings = np.array(embeddings)
# Mean pooling to get a single embedding for the sentence
sentence_embedding = np.mean(embeddings, axis=1)[0]
print(sentence_embedding)
# print(len(x[0]))
# print(type(x[0]))
# pprint(x[0])




# # Classing sentence_transformers problem
# from sentence_transformers import SentenceTransformer
# sentences = ["This is an example sentence", "Each sentence is converted"]

# model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
# embeddings = model.encode(sentences)
# print(embeddings)