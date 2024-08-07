from pyspark.sql import DataFrame, SparkSession
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, ArrayType
from pyspark.sql.functions import udf, collect_list
from lagoon_translator.reducers.Reducer import Reducer

class NCCustReducer(Reducer):
    def __init__(self):
        super(NCCustReducer, self).__init__(self.__class__.__name__)

    def reduce(self, spark_session: SparkSession) -> DataFrame:
        catalog_name = "rest_catalog"
        namespace = "ncentral"

        spark_session.sql(f"USE {catalog_name}")  # mandatory

        # ---------------------------------- Computations ----------------------------------
        customers = spark_session.sql(f"SELECT * FROM {namespace}.customers")
        devices = spark_session.sql(f"SELECT * FROM {namespace}.devices")
        dev_stats = spark_session.sql(f"SELECT * FROM {namespace}.device_statistics")

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
