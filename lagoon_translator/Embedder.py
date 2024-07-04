class Embedder:
    def __init__(self, name, dimensions):
        self.name = name
        self.dim = dimensions

    def embed(self, text: str):
        raise NotImplementedError

    