import pprint

from pyspark.sql.functions import udf, collect_list
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

from lagoon_translator.config import *
from lagoon_translator.spark_maker import sparky
import logging
import os
os.environ["AWS_REGION"] = "bamba"
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger("Connectwise Lakehouse")
logger.warning("starting")


spark = sparky()
spark.sparkContext.setLogLevel("ERROR")

print(spark.version)
spark.sql(f"USE {catalog_name}")

# ---------------------------------- Computations ----------------------------------
customers = spark.sql(f"SELECT * FROM {namespace}.customers")
devices = spark.sql(f"SELECT * FROM {namespace}.devices")
dev_stats = spark.sql(f"SELECT * FROM {namespace}.device_statistics")


dev_stat_cols = dev_stats.columns

@udf(returnType=StringType())
def stringify_dev_stat(*vals):
    inter_list = [f"{dev_stat_cols[i]}: {vals[i]}, " for i in range(len(vals))]
    str_res = "(device statistic follows) " + ''.join(inter_list)
    return str_res

@udf(returnType=StringType())
def concat_dev_stats(strlist):
    inter_list = [f"{strlist[i]}\n" for i in range(len(strlist))]
    str_res = ''.join(inter_list)
    return str_res


dev_stats_with_str = (dev_stats.withColumn("string", stringify_dev_stat(*dev_stat_cols))
     .select("device_id", "string"))

dev_stats_with_str.show(3, vertical=True, truncate=False)

dev_stats_with_str_grouped = dev_stats_with_str.groupBy("device_id").agg(
    concat_dev_stats(collect_list("string")).alias("dev_stats_string")).withColumnRenamed("device_id", "device_id_X")

dev_stats_with_str_grouped.show(3, vertical=True, truncate=False)

first_join = devices.join(dev_stats_with_str_grouped, devices.device_id == dev_stats_with_str_grouped.device_id_X,
                          how="inner")

first_join.show(3, vertical=True, truncate=False)

dev_cols = first_join.columns
@udf(returnType=StringType())
def stringify_dev(*vals):
    inter_list = [f"{dev_cols[i]}: {vals[i]} \n\n" for i in range(len(vals))]
    str_res = "(device follows) " + ''.join(inter_list)
    return str_res

@udf(returnType=StringType())
def concat_dev(strlist):
    # print(f"strlist: {strlist}")
    inter_list = [f"{strlist[i]}\n\n\n" for i in range(len(strlist))]
    str_res = ''.join(inter_list)
    return str_res

dev_stringified = (first_join.withColumn("dev_sting", stringify_dev(*dev_cols)).select("customer_id", "dev_sting"))


dev_stringified.show(3, vertical=True, truncate=False)

dev_stringified_grouped = (dev_stringified.groupby("customer_id")
                           .agg(collect_list(dev_stringified.dev_sting).alias("devs_str_arr"))
                           .withColumn("devs_str", concat_dev("devs_str_arr"))
                           .withColumnRenamed("customer_id", "customer_id_X")
                           .select("customer_id_X", "devs_str")
                           )

dev_stringified_grouped.show(3, vertical=True, truncate=False)


second_join = customers.join(dev_stringified_grouped, customers.customer_id == dev_stringified_grouped.customer_id_X,
                             how="inner")
second_join.show(3, vertical=True, truncate=False)


cust_cols = second_join.columns
@udf(returnType=StringType())
def stringify_cust(*vals):
    inter_list = [f"{cust_cols[i]}: {vals[i]} \n\n\n\n " for i in range(len(vals))]
    str_res = "(customer follows) " + ''.join(inter_list)
    return str_res

customers_stringified = second_join.withColumn("cust_str", stringify_cust(*cust_cols)).select("customer_id", "cust_str")

customers_stringified.show(3, vertical=True, truncate=False)

cust_strings = customers_stringified.take(5)
x = cust_strings[0].asDict()["cust_str"]

with open("Output.txt", "w") as text_file:
    text_file.write(x)
