import sys
sys.path += ["/Users/mimischly/Desktop/bluebird/jun03/Translation"]

from typing import List
from src.Document import Document


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
    

class QDrantIngestor(Ingestor):
    def __init__(self, host, port):
        name="qdrant_ingestor"
        super(QDrantIngestor, self).__init__(name=name, host=host, port=port)

    # def connect/


    


