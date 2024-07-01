import sys
sys.path.insert(0, "/Users/mimischly/Desktop/bluebird/jun03/Translation/")

from src.translators.NCCustTranslator import NCCustTranslator, Translator
from src.ingestors.QDrantIngestor import QDrantIngestor
from src.ingestors.ElasticIngestor import ElasticIngestor
from dotenv import load_dotenv
import os
from src.spark_maker import sparky
from src.ingestors.embeddors.TrivialEmbedder import TrivialEmbedder
from src.documators.NCCustVectDocumator import NCCustVectDocumator

load_dotenv()

def elastic():

  ingestor = ElasticIngestor(os.environ['ELASTIC_HOST'], os.environ['ELASTIC_PORT'])

  trans = NCCustTranslator(ingestor)

  spark_session = sparky()

  # df = trans.transform(spark_session)
  # doc = trans.documentify(df.take(1)[0])
  # print(doc)
  # trans.ingest([doc])

  trans.run(spark_session)

  """
  Calling the `connect` method of an Ingestor before passing to a Translator will leads to the serialization error

  ```
  Traceback (most recent call last):                                              
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/serializers.py", line 459, in dumps
      return cloudpickle.dumps(obj, pickle_protocol)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/cloudpickle/cloudpickle_fast.py", line 73, in dumps
      cp.dump(obj)
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/cloudpickle/cloudpickle_fast.py", line 632, in dump
      return Pickler.dump(self, obj)
            ^^^^^^^^^^^^^^^^^^^^^^^
  TypeError: cannot pickle '_thread._local' object
  Traceback (most recent call last):
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/serializers.py", line 459, in dumps
      return cloudpickle.dumps(obj, pickle_protocol)
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/cloudpickle/cloudpickle_fast.py", line 73, in dumps
      cp.dump(obj)
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/cloudpickle/cloudpickle_fast.py", line 632, in dump
      return Pickler.dump(self, obj)
            ^^^^^^^^^^^^^^^^^^^^^^^
  TypeError: cannot pickle '_thread._local' object

  During handling of the above exception, another exception occurred:

  Traceback (most recent call last):
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/main.py", line 22, in <module>
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/Translator.py", line 63, in run
      transformed_df.foreachPartition(_process_batch)
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/sql/dataframe.py", line 1489, in foreachPartition
      self.rdd.foreachPartition(f)  # type: ignore[arg-type]
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 1801, in foreachPartition
      self.mapPartitions(func).count()  # Force evaluation
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 2316, in count
      return self.mapPartitions(lambda i: [sum(1 for _ in i)]).sum()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 2291, in sum
      return self.mapPartitions(lambda x: [sum(x)]).fold(  # type: ignore[return-value]
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 2044, in fold
      vals = self.mapPartitions(func).collect()
            ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 1833, in collect
      sock_info = self.ctx._jvm.PythonRDD.collectAndServe(self._jrdd.rdd())
                                                          ^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 5470, in _jrdd
      wrapped_func = _wrap_function(
                    ^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 5268, in _wrap_function
      pickled_command, broadcast_vars, env, includes = _prepare_for_python_RDD(sc, command)
                                                      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/rdd.py", line 5251, in _prepare_for_python_RDD
      pickled_command = ser.dumps(command)
                        ^^^^^^^^^^^^^^^^^^
    File "/Users/mimischly/Desktop/bluebird/jun03/Translation/.venv/lib/python3.11/site-packages/pyspark/serializers.py", line 469, in dumps
      raise pickle.PicklingError(msg)
  _pickle.PicklingError: Could not serialize object: TypeError: cannot pickle '_thread._local' object
  ```


  But if you start and close the connection within a method of Translator everything works perfect!

  """



def qd():
  embedder = TrivialEmbedder()
  ingestor = QDrantIngestor(os.environ['ELASTIC_HOST'], os.environ['ELASTIC_PORT'], embedder)

  print("ingestor created!")

  trans = NCCustTranslator(ingestor)

  print("translator created!")

  spark_session = sparky()
  
  print("sparky created!")

  trans.run(spark_session)

  print("done!")


def new_try_qdrant():
  embedder = TrivialEmbedder()
  ingestor = QDrantIngestor(os.environ['ELASTIC_HOST'], os.environ['ELASTIC_PORT'], embedder)
  documator = NCCustVectDocumator("xxx")

  print("ingestor and documator created!")

  # trans = NCCustTranslator(ingestor)
  trans = Translator(ingestor, documator)

  print("translator created!")

  spark_session = sparky()
  
  print("sparky created!")

  trans.run(spark_session)

  print("done!")


def new_try_elastic():
  ingestor = ElasticIngestor(os.environ['ELASTIC_HOST'], os.environ['ELASTIC_PORT'])
  documator = NCCustVectDocumator("xxx")

  trans = Translator(ingestor, documator)

  spark_session = sparky()

  # df = trans.transform(spark_session)
  # doc = trans.documentify(df.take(1)[0])
  # print(doc)
  # trans.ingest([doc])

  trans.run(spark_session)

if __name__ == "__main__":
  # qd()
  new_try_elastic()