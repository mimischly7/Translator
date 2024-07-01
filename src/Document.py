class Document:
    def __init__(self, content: str, payload: dict, collection: str):
        self.content = content
        self.payload = payload
        self.collection = collection

    def get_content(self):
        return self.content

    def get_payload(self):
        return self.payload

    def get_collection(self):
        return self.collection

    def unify(self):
        return {**self.payload, "content": self.content}
    
    def __repr__(self):
        return {**self.unify(), "collection" : self.collection}

    def __str__(self):
        return str(self.__repr__().keys())
    

    