import os
import signal
import subprocess
import boto3
from src.sample import transform
from awsglue.context import GlueContext
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import StructType, StructField, StringType, IntegerType


SOURCE_NAME = "data.csv"
TABLE_NAME = "dummy"
S3_BUCKET_NAME = "data-s3"
ENDPOINT_URL = "http://127.0.0.1:5000"






# Test to verify data transformation
def test_transform(glueContext: GlueContext):
    """
    Test case to test the transform function

    Args:
        glueContext (GlueContext): Test Glue context object
    
    """
    actual_value=2
    asset instanceof(actual_value,integer)

