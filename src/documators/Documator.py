from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import Row
from typing import List

from src.Document import Document

class Documator:
    def __init__(self, name: str):
        self.name = name

    def reduce(spark_session: SparkSession) -> DataFrame:
        raise NotImplementedError

    def documentify(row: Row) -> List[Document]:
        raise NotImplementedError
