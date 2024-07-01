from typing import List
from dotenv import load_dotenv
import os

from qdrant_client import QdrantClient

import sys
sys.path.insert(0, "/Users/mimischly/Desktop/bluebird/jun03/Translation")

from src.ingestors.Ingestor import Ingestor
from src.Document import Document
from src.ingestors.embeddors.Embedder import Embedder

load_dotenv()

from qdrant_client import models, QdrantClient
# from sentence_transformers import SentenceTransformer
# encoder = SentenceTransformer("all-MiniLM-L6-v2")



class QDrantIngestor(Ingestor):
    def __init__(self, host, port, embedder: Embedder):
        name = "qdrant_ingestor"
        self.embedder = embedder
        super(QDrantIngestor, self).__init__(name=name, host=host, port=port)
    
    def connect(self):
        if not hasattr(self, "client"):
            self.client = QdrantClient("http://localhost:6333")

    def disconnect(self):
        if hasattr(self, "client"):
            self.client.close()
        else:
            raise Exception("No connection to QDrant client exists yet!")
        

    def storeDocument(self, doc: Document):
        self._create_collection(doc.collection)
        self.client.upload_points(
            collection_name=doc.collection,
            points=[
                models.PointStruct(
                    id=idx, vector=self.embedder.embed(doc).tolist(), payload=doc.payload
                )
                for idx, doc in enumerate([doc])
            ],
        )
    
    def storeDocumentBatch(self, docs: List[Document]):
        self._create_collection(docs[0].collection)
        print("about to store batch of docs")
        print(self.embedder.embed(docs[0].content))
        response = self.client.upload_points(
            collection_name=docs[0].collection,
            points=[
                models.PointStruct(
                    id=idx, vector=self.embedder.embed(doc.content), payload=doc.payload
                )
                for idx, doc in enumerate(docs)
            ],
        )
        print(f"response: {response}")

    # just for testing
    def _search(self, text):
        pass

    def _create_collection(self, collection_name: str):
        if not self.client.collection_exists(collection_name):
            self.client.create_collection(
            collection_name=collection_name,
            vectors_config=models.VectorParams(
                size=self.embedder.dim,  # Vector size is defined by used model
                distance=models.Distance.COSINE,
            ),
        )

