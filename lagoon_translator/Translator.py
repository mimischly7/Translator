from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import Row
from typing import List

from lagoon_translator.Document import Document
from lagoon_translator.ingestors.Ingestor import Ingestor
from lagoon_translator.documators import Documator
from lagoon_translator.reducers import Reducer

class Translator:
    """
    Orchestration class that receives a :class:`Documentator` and an :class:`Ingestor` to take us from Iceberg tables
    to succesfull storage in our store of choice. The `run` method performs this orchestration.

    Steps:
        1. Transform: 
            Transform the related spark dataframes to produce a `content` column, where each cell contains the tree 
            representation (using nested spark StructType's and ArrayType's) of the document that is to be stored to the vector/keyword
            engine.
            (`_transform` method)
        2. Document: 
            Given the transformed Spark DataFrame, which contractually has a `content` column, produce a :class:`Document` for each
            value of that column (a :class:`Document` is a thin wrapper for the document content, some metadata, and the collection/index
            it belongs to). 
            (`_documentify` method)
        3. Ingest:
            Given documents produces in step (2), store these documents in the desired endstore. This is where the `ingestor` attribute
            comes in.
            (`_ingest` method)
    
    Although this is the logical order of the steps, steps (2) and (3) will operate on batches (partitions) of the relevant data,
    so in a way they will happen in parallel (although for each batch they will run in the specified order)
    """
    def __init__(self, ingestor: Ingestor, reducer: Reducer, documator: Documator):
        self.reducer = reducer
        self.ingestor = ingestor
        self.documator = documator

    def _transform(self, spark_session: SparkSession) -> DataFrame:
        return self.reducer.reduce(spark_session)

    def _documentify(self, row: Row) -> List[Document]:
        return self.documator.documentify(row, )
    
    def _ingest(self, docs: List[Document]):
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
            docs = [doc for row in itr for doc in self._documentify(row)]
            self._ingest(docs)

        transformed_df = self._transform(spark_session)
        transformed_df.foreachPartition(_process_batch)