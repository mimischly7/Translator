from pyspark.sql import DataFrame, SparkSession

class Reducer:
    def __init__(self, name: str):
        self.name = name

    def reduce(spark_session: SparkSession) -> DataFrame:
        raise NotImplementedError
