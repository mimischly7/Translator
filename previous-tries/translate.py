import pprint
from jinja2 import Template
from pyspark.sql.functions import udf, collect_list
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType, Row
from lagoon_translator.config import *
from lagoon_translator.spark_maker import sparky
from lagoon_translator.templates.ncentral_template import *
from pyspark.sql import DataFrame, SparkSession
from lagoon_translator.Document import Document
from lagoon_translator.ingestors.ElasticIngestor import ElasticIngestor
from dotenv import load_dotenv
import os
import time
from dotenv import load_dotenv
from lagoon_translator.utils import *
load_dotenv()

spark = sparky()

def transform(spark: SparkSession) -> DataFrame:
    spark.sql(f"USE {catalog_name}")  # mandatory

    # ---------------------------------- Computations ----------------------------------
    customers = spark.sql(f"SELECT * FROM {namespace}.customers")
    devices = spark.sql(f"SELECT * FROM {namespace}.devices")
    dev_stats = spark.sql(f"SELECT * FROM {namespace}.device_statistics")

    # -------------------------------------------------------------------------
    # ----------------------- Device Statistics -------------------------------
    # -------------------------------------------------------------------------
    dev_stat_cols = dev_stats.columns

    # Create dev-stats struct
    device_stats_struct = StructType()
    for dev_stat_field in dev_stat_cols:
        device_stats_struct.add(dev_stat_field, StringType())


    @udf(returnType=device_stats_struct)
    def structify_dev_stat(*vals):
        d = {dev_stat_cols[i]: vals[i] for i in range(len(dev_stat_cols))}
        return d


    dev_stats_with_struct = (
        dev_stats.withColumn("dev_stat_struct", structify_dev_stat(*dev_stat_cols)).select("device_id", "dev_stat_struct")
    )

    dev_stats_with_struct_grouped = (
        dev_stats_with_struct.groupby("device_id").agg(collect_list("dev_stat_struct").alias("dev_stat_structs"))
        .withColumnRenamed("device_id", "device_id_X")
    )

    # -------------------------------------------------------------------------
    # --------------------------------- Devices -------------------------------
    # -------------------------------------------------------------------------
    dev_join_stats = devices.join(
        dev_stats_with_struct_grouped, devices["device_id"] == dev_stats_with_struct_grouped["device_id_X"], how="inner")

    # Create devs struct
    device_struct = StructType()
    for dev_field in devices.columns:
        device_struct.add(dev_field, StringType())
    device_struct.add("dev_stat_structs", ArrayType(device_stats_struct))  # this is the column created, not in orig table

    dev_cols = dev_join_stats.columns


    @udf(returnType=device_struct)
    def structify_dev(*vals):
        d = {dev_cols[i]: vals[i] for i in range(len(dev_cols))}
        return d


    devs_with_struct = dev_join_stats.withColumn("dev_struct",
                                                structify_dev(*dev_join_stats.columns)).select("customer_id", "dev_struct")
    devs_with_struct_grouped = (devs_with_struct.groupby("customer_id").agg(collect_list("dev_struct").alias("dev_structs"))
                                .withColumnRenamed("customer_id", "customer_id_X"))


    # -------------------------------------------------------------------------
    # --------------------------------- Customers -------------------------------
    # -------------------------------------------------------------------------
    cust_join_devs = customers.join(devs_with_struct_grouped,
                                    customers["customer_id"] == devs_with_struct_grouped["customer_id_X"],
                                    how="inner")

    cust_cols = cust_join_devs.columns

    # Create customers struct
    cust_struct = StructType()
    for cust_field in customers.columns:
        cust_struct.add(cust_field, StringType())
    cust_struct.add("dev_structs", ArrayType(device_struct))


    @udf(returnType=cust_struct)
    def structify_cust(*vals):
        d = {cust_cols[i]: vals[i] for i in range(len(cust_cols))}
        return d


    custs_with_struct = (cust_join_devs.withColumn("cust_struct", structify_cust(*cust_join_devs.columns))
                        .select("customer_id", "cust_struct"))
    
    return custs_with_struct




custs_with_struct = transform(spark)

# print(custs_with_struct.columns)
# cust_structs = [ recursive_dictify(row)['cust_struct'] for row in custs_with_struct.collect() ]

# data = [{"data": cs, "metadata": {"num_devices": len(cs["dev_structs"])}} for cs in cust_structs]

# template = Template(jinja_template)
# formatted_text = template.render(cust_struct=data[2]["data"], meta=data[2]["metadata"])


# with open("Output.md", "w") as text_file:
#     text_file.write(formatted_text)

# print("done")



cust = custs_with_struct.take(1)[0]



### 1: convert the map-like object to a string
content = recursive_dictify(cust)['cust_struct']
template = Template(jinja_template)
data = {"data": content, "metadata": {"num_devices": len(content["dev_structs"])}}
formatted_text = template.render(cust_struct=data["data"], meta=data["metadata"])
data_for_doc = {
    "content" : str(formatted_text),
    "payload" : {"summary" : f"NCentral information for customer {content['customer_id']}"},
    "collection" : "customers"
}

# print(formatted_text)

### 2: use the formatted string (and other info) to produce a Document object
doc = Document(content = data_for_doc["content"], payload = data_for_doc["payload"], collection = data_for_doc["collection"])
print(doc)

### 3: Given the Document object, use the Ingestor to store it to qdrant/elastic
es = ElasticIngestor(os.environ["ELASTIC_HOST"], os.environ["ELASTIC_PORT"])
es.connect()
es._create_index(index_name="customers", force=True)
es.other()
print("asdad", doc)
es.storeDocument(doc)

time.sleep(4)
print("Search results: ")
search_results = es._search("Aafiyat Medical")
# print(search_results)






# def ingest(dataframe: DataFrame):
    # dataframe.take()

# def f(itr):
#     print(itr)
#     print(type(itr))
#     for i in itr:
#         # print(i)
#         print(type(i))
#         print(len(i))

# custs_with_struct.foreachPartition(f)