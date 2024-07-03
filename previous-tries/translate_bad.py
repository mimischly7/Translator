import pprint

from pyspark.sql.functions import udf
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


dev_stats_struct = StructType(
    [
        StructField("appliance_id", IntegerType(), True),
        StructField("appliance_name", StringType(), True),
        StructField("device_id", IntegerType(), True),
        StructField("task_id", IntegerType(), True),
    ]
)


print(dev_stats_struct)
dev_stat_columns = dev_stats.columns

print(dev_stat_columns)

customers.show(3)
devices.show(3)
dev_stats.show(3)


def dev_stats_combine(task_id, device_id, appliance_name, appliance_id):
    return {
        "appliance_id": appliance_id,
        "device_id": device_id,
        "task_id": task_id,
        "appliance_name": appliance_name
    }

dev_stats_combine_udf = udf(dev_stats_combine, dev_stats_struct)

x = (dev_stats.withColumn("xxx", dev_stats_combine_udf("task_id", "device_id", "appliance_name", "appliance_id"))
     .select("device_id", "task_id", "xxx"))

x.show(3, vertical=True, truncate=False)
print(x.schema)
p = x.take(2)
pprint.pprint([y.asDict() for y in p])



