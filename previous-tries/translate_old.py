import pprint

from pyspark.sql import SparkSession
from pyspark.sql.functions import udf, struct, col, collect_list, min
from pyspark.sql.types import StringType, ArrayType
from lagoon_translator.config import *

import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Connectwise Lakehouse")
logger.warning("starting")

import os

os.environ["AWS_REGION"] = "bamba"

spark = (
    SparkSession.builder
    .config("spark.jars.packages",
            "org.apache.spark:spark-sql_2.12:3.5.1,"
            "org.apache.hadoop:hadoop-aws:3.3.4,"
            "org.apache.hadoop:hadoop-client-runtime:3.3.4,"
            "software.amazon.awssdk:bundle:2.23.19,"
            "org.apache.iceberg:iceberg-spark-runtime-3.5_2.12:1.5.2,")
    #    // Iceberg Catalog Configuration
    .config("spark.sql.extensions",
            "org.apache.iceberg.spark.extensions.IcebergSparkSessionExtensions")  # Use Iceberg with Spark
    .config(f"spark.sql.catalog.{catalog_name}", "org.apache.iceberg.spark.SparkCatalog")
    .config(f"spark.sql.catalog.{catalog_name}.type", "rest")
    .config(f"spark.sql.catalog.{catalog_name}.uri", f"http://{rest_endpoint}/")
    .config(f"spark.sql.catalog.{catalog_name}.warehouse", f"s3a://{bucket}")
    #  MinIO-Specific Configurations (for both Iceberg and Hadoop)
    .config(f"spark.sql.catalog.{catalog_name}.hadoop.fs.s3a.endpoint", f"http://{minio_endpoint}")
    .config(f"spark.sql.catalog.{catalog_name}.s3.endpoint", f"http://{minio_endpoint}")  # Added for Iceberg
    .config(f"spark.hadoop.fs.s3a.endpoint", f"http://{minio_endpoint}")
    # MinIO Credentials
    .config(f"spark.sql.catalog.{catalog_name}.hadoop.fs.s3a.access.key", access_key)
    .config(f"spark.sql.catalog.{catalog_name}.hadoop.fs.s3a.secret.key", secret_key)
    .config(f"spark.sql.catalog.{catalog_name}.s3.access-key-id", access_key)
    .config(f"spark.sql.catalog.{catalog_name}.s3.secret-access-key", secret_key)
    .config("spark.hadoop.fs.s3a.access.key", access_key)
    .config("spark.hadoop.fs.s3a.secret.key", secret_key)
    # Additional S3 Configurations
    .config("spark.hadoop.fs.s3a.path.style.access", "true")
    .config("spark.hadoop.fs.s3a.connection.establish.timeout", "15000")
    .config("spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    # Ensure Iceberg uses the correct S3 FileIO implementat
    # ion
    .config(f"spark.sql.catalog.{catalog_name}.io-impl", "org.apache.iceberg.aws.s3.S3FileIO")
    .getOrCreate()
)
# print(spark.version)
spark.sparkContext.setLogLevel("ERROR")

print(spark.version)
spark.sql(f"USE {catalog_name}")

# Computations
dev_stats = spark.sql(f"SELECT * FROM {namespace}.device_statistics")

dev_stat_columns = dev_stats.columns


# def concat_row(*row):
#     vals = list(map(lambda x: str(x), row))
#     dev_stat_text = []
#     for i in range(len(vals)):
#         dev_stat_text.append(f'''{dev_stat_columns[i]}: {vals[i]},  ''')
#     return dev_stat_text

def concat_row(*row):
    vals = list(map(lambda x: str(x), row))
    dev_stat_text = []
    for i in range(len(vals)):
        dev_stat_text.append(f'''{dev_stat_columns[i]}: {vals[i]},  ''')
    return ''.join(dev_stat_text)

concat_row_udf = udf(concat_row, StringType())

dev_stats_flat = (dev_stats.withColumn("device_stats_str", concat_row_udf(*[col(x) for x in dev_stats.columns])).
                  select("device_id", "device_stats_str")).withColumnRenamed("device_id", "device_id_X")
# dev_stats.show()
# dev_stats_flat.show(5, truncate=False, vertical=True)

# x = dev_stats_flat.agg(collect_list(dev_stats_flat["device_id"]),
#                        collect_list(dev_stats_flat["device_stats_str"])).collect()
# print(x)
# print(type(x))
# print(len(x))
# print(type(x[0]))

dev_stats_flat_grouped = (dev_stats_flat.groupby("device_id_X")
                          .agg(collect_list("device_stats_str").alias("device_statistics")))
dev_stats_flat_grouped.show(3, truncate=False, vertical=True)
x = dev_stats_flat_grouped.collect()
print(x[0])
print(type(x[0]))
rowDict = x[0].asDict()
print(rowDict)
print(rowDict['device_statistics'])
print(len(rowDict['device_statistics']))

devices = spark.sql(f"SELECT * FROM {namespace}.devices")

dev_stats_join = devices.join(dev_stats_flat_grouped, devices.device_id == dev_stats_flat_grouped.device_id_X)

dev_stats_join.show(5, truncate=False, vertical=True)


dev_join_cols = dev_stats_join.columns
def concat_row_2(*row):
    vals = list(map(lambda x: str(x), row))
    dev_stat_text = []
    for i in range(len(vals)):
        dev_stat_text.append(f'''{dev_join_cols[i]}: {vals[i]},  ''')
    return ''.join(dev_stat_text)

concat_row_2_udf = udf(concat_row_2, StringType())

devices_flat = (dev_stats_join.withColumn("dev_str", concat_row_2_udf(*dev_join_cols))
                .select("device_id", "customer_id", "dev_str"))

devices_flat.show(3, truncate=False, vertical=True)

devices_flat_grouped = (devices_flat.select("customer_id", "dev_str").
                        groupby("customer_id").agg(collect_list("dev_str").alias("dev_str_list")))

devices_flat_grouped.show(3, truncate=False, vertical=True)








#
# print(devices.where(devices.device_id in dev_stats_flat_grouped.device_id ))
# print(dev_stats_join.count())

# pprint.pprint(x)

# devices = spark.sql(f"SELECT * FROM {namespace}.devices")
#
# dev_stats_join = devices.join(
#     dev_stats_flat,  # Dataset / dataframe
#     devices.device_id == dev_stats_flat.device_id_X,  # This is same as ON in SQL,
#     "left")
#
# dev_stats_join.show(5, vertical=True, truncate=False)

# columns2 = dev_stats_join.columns
# def concat_row_2(*row):
#     vals = list(map(lambda x: str(x), row))
#     dev_stat_text = ''
#     for i in range(len(vals)):
#         new_text = f'''{columns2[i]}: {vals[i]}\n '''
#         dev_stat_text += new_text
#     return dev_stat_text
#
#
# concat_row_udf_2 = udf(concat_row_2, StringType())
#
# devices_flat = dev_stats_join.select("device_id", concat_row_udf_2(*dev_stats_join.columns).alias("string"))
# devices_flat.show(5, vertical=True, truncate=False)







# # Suppress Spark logging
# logger = logging.getLogger('py4j')
# logger.setLevel(logging.ERROR)
# # Optional: Turn off other Spark-related logs
# logging.getLogger('pyspark').setLevel(logging.ERROR)
# logging.getLogger('pyspark.sql').setLevel(logging.ERROR)


# spark.sql(f"SELECT * FROM {namespace}.{table_name}")
# spark.sql(f"USE {catalog_name}")
# # print(spark.sql(f"-- SELECT * FROM ..."))
# spark.sql(f"USE {catalog_name}")
# tables = spark.sql(f"SHOW TABLES IN {namespace}")
# print(tables.show())

# service_orgs = spark.sql(f"SELECT * FROM {namespace}.service_orgs")
# customers = spark.sql(f"SELECT * FROM {namespace}.customers")
# devices = spark.sql(f"SELECT * FROM {namespace}.devices")
# device_statistics = spark.sql(f"SELECT * FROM {namespace}.device_statistics")


# print(service_orgs.show(10))
# print(customers.show(10))
# print(devices.show(10))
# print(device_statistics.show(10))

# join_query = \
#  f'''
#  SELECT *
#  FROM {namespace}.customers
# --    LEFT JOIN {namespace}.devices ON {namespace}.customers.customer_id = {namespace}.devices.customer_id
# --    LEFT JOIN {namespace}.device_statistics ON {namespace}.devices.device_id = {namespace}.device_statistics.device_id
# --    GROUP BY  {namespace}.customers.customer_id
#  '''
#
# joined = spark.sql(join_query)
#
#
#
# # print("customer-count: ", customers.count())
# # print("devices-count: ", devices.count())
# print("customers_devices-count: ", joined.count())
#
# print(joined.show(10, vertical=True))
# print("kkk: ", joined.count())
#
# grouped = joined.groupBy(f"{namespace}.customers.customer_id").count()
# print(grouped.show(10, vertical=True))
# print("popopopo")
# print(joined.show(10))
# print("kkk: ", joined.count())
# print("ggg: ", grouped.)

# pprint.pprint([x.asDict() for x in joined.take(3)])
# grouped = joined.groupBy("customers.customer_id")
# print("aaa: ", grouped.count())
# print(joined.show(10))


# SOS: https://danvatterott.com/blog/2018/09/06/python-aggregate-udfs-in-pyspark/