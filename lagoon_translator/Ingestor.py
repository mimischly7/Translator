import sys

from typing import List
from lagoon_translator.Document import Document

class Ingestor:
    def __init__(self, name, host, port):
        self.name = name
        self.host = host
        self.port = port

    def connect():
        raise NotImplementedError
    
    def disconnect():
        raise NotImplementedError

    def storeDocument(doc: Document):
        raise NotImplementedError
    
    def storeDocumentBatch(docs: List[Document]):
        raise NotImplementedError
    
    def httpify(self):
        return f'http://{self.host}:{self.port}'
    