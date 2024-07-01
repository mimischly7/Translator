from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import Row
from typing import List

from src.Document import Document
from src.ingestors.Ingestor import Ingestor
from src.config import *

class Translator:
    def __init__(self, ingestor: Ingestor):
        self.ingestor = ingestor

    def transform(spark_session: SparkSession) -> DataFrame:
        raise NotImplementedError

    def documentify(row: Row) -> Document:
        raise NotImplementedError
    
    def ingest(self, docs: List[Document]):
        self.ingestor.connect()
        self.ingestor.storeDocumentBatch(docs)
        self.ingestor.disconnect()

    def run(self, spark_session: SparkSession):
        """
        SOS (serialization in the context of distributed computing):
        
        In the context of distributed computing systems, like Spark, when you want to perform some computation, this must
        happen in the nodes. For this to happen, the DRIVER node must somehow transmit (1) the data to be processed and
        (2) the code based on which the data will be processed to these nodes. In order for this transmission to happen,
        the driver node must SERIALIZE the data and the code so it can be transmitted over the network, and the nodes that
        receive this will in turn DESERIALIZE it to perform the job necessary.

        For this reason, it is important to make sure that the CODE you want the nodes to use are serializable. One thing
        that is generally not serializable are CONNECTIONS, e.g. database connections. The reason is that objects that maintain
        some sort of connection to a source are tied to the specific environment in which they are created (e.g. host machine),
        so any attempts to serialization would break their state.
        
        In this case, I am using `<df>.foreachPartition(<some-func>)`, which will attempt to serialize both the dataframe partition 
        AND the code of <some-func> to transmit to the nodes. Therefore,  <some-func> has to be serializable. Initially, my code
        for <some-func> included usage of `self` (a `Translator` object), which in turn had as an attribute an object that maintained
        a connection to the ElasticSearch engine.

        To solve the problem, I created a new connection to the engine form within <some-func> (which makes sense, because each node
        should have its own connection to the search engine), and when I had to use a bound method (a function bound to the class, 
        e.g. self.documentify), I instead took the __func__ attribute and used that with None in the place of self (equivalent to
        <classname>.func(None, ...)).

        **BETTER SOLUTION**
        Start and close connection with a method the enclosing class (the Translator.ingest method in this case) instead of before
        passing the Ingestor object to Translator!
        """
        # # Old solution
        # doc_func = self.documentify.__func__
        # ingest_func = self.ingest.__func__
        # def _process_batch(itr):
        #     docs = [doc_func(None, row) for row in itr]
        #     ingest_func(None, docs)

        # Better Solution
        def _process_batch(itr):
            docs = [self.documentify(row) for row in itr]
            self.ingest(docs)

        transformed_df = self.transform(spark_session)
        transformed_df.foreachPartition(_process_batch)