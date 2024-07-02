from pyspark.sql import SparkSession
from src.config import *
import os

def sparky() :
    spark_session = (SparkSession.builder
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
    .getOrCreate())

    spark_session.sparkContext.setLogLevel("ERROR")
    return spark_session

os.environ["AWS_REGION"] = "bamba"
# logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# logger = logging.getLogger("Connectwise Lakehouse")
# logger.warning("starting")
