from pyspark.sql.types import Row
from typing import List

from lagoon_translator.Document import Document

class Documator:
    def __init__(self, name: str, template: str):
        self.name = name
        self.template = template

    def documentify(row: Row, template: str) -> List[Document]:
        raise NotImplementedError
