from elasticsearch import Elasticsearch
from pprint import pprint
from typing import List

from lagoon_translator.ingestors.Ingestor import Ingestor
from lagoon_translator.Document import Document


class ElasticIngestor(Ingestor):
    def __init__(self, host, port):
        name = "elasticsearch"
        super(ElasticIngestor, self).__init__(name=name, host=host, port=port)
    
    def connect(self):
        if not hasattr(self, "es"):
            self.es = Elasticsearch(self.httpify())  # <-- connection options need to be added here
            client_info = self.es.info()
            print('Connected to Elasticsearch!')
            pprint(client_info.body)

    def disconnect(self):
        if hasattr(self, "es"):
            self.es.close()

    def storeDocument(self, doc: Document):
        doc_dict = doc.unify()
        print("zzzz")
        pprint(doc_dict)
        print(doc.collection)
        response = self.es.index(index=doc.collection, body=doc_dict)
        print(response['_id'])
    
    def storeDocumentBatch(self, docs: List[Document]):
        operations = []
        for doc in docs:
            operations.append({'index': {'_index': doc.collection}})
            operations.append(doc.unify())
        return self.es.bulk(operations=operations)
    
    def _create_index(self, index_name: str, force=False) -> None:
        if (not self.es.indices.exists(index=index_name)) or force:
            self.es.indices.delete(index=index_name, ignore_unavailable=True)
            self.es.indices.create(index=index_name)

    def other(self):
        print(self.es.indices.get(index="customers"))
        print(self.es.indices)
        print(type(self.es.indices))

    # just for testing
    def _search(self, text):
        results = self.es.search(
            index='customers',
            query= {
                "match": {
                    "content": {
                        "query": "Aafiyat Medical"
                    }
                }
            }
        )
        
        print("results: ")
        print(results)
        print("???")
        return results['hits']['hits']
    