import os
from pyspark.sql import *
from pyspark.sql.functions import unix_timestamp, udf, to_date
from pyspark.sql.types import *
from datetime import datetime
spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

GKG_SCHEMA = StructType([
        StructField("GKGRECORDID",StringType(),True),
        StructField("DATE",StringType(),True),
        StructField("SourceCollectionIdentifier",StringType(),True),
        StructField("SourceCommonName",StringType(),True),
        StructField("DocumentIdentifier",StringType(),True),
        StructField("Counts",StringType(),True),
        StructField("V2Counts",StringType(),True),
        StructField("Themes",StringType(),True),
        StructField("V2Themes",StringType(),True),
        StructField("Locations",StringType(),True),
        StructField("V2Locations",StringType(),True),
        StructField("Persons",StringType(),True),
        StructField("V2Persons",StringType(),True),
        StructField("Organizations",StringType(),True),
        StructField("V2Organizations",StringType(),True),
        StructField("V2Tone",StringType(),True),
        StructField("Dates",StringType(),True),
        StructField("GCAM",StringType(),True),
        StructField("SharingImage",StringType(),True),
        StructField("RelatedImages",StringType(),True),
        StructField("SocialImageEmbeds",StringType(),True),
        StructField("SocialVideoEmbeds",StringType(),True),
        StructField("Quotations",StringType(),True),
        StructField("AllNames",StringType(),True),
        StructField("Amounts",StringType(),True),
        StructField("TranslationInfo",StringType(),True),
        StructField("Extras",StringType(),True)
        ])

DATA_DIR="hdfs:///datasets/gdeltv2"

spark_df = spark.read.option("delimiter", "\t").csv(schema=GKG_SCHEMA, path=os.path.join(DATA_DIR, "*.gkg.csv"))

filtered_df = spark_df.filter( ( spark_df["V2Themes"].contains("REFUGEE") ) ).select("GKGRECORDID",
"DATE",
"SourceCommonName",
"DocumentIdentifier",
"V2Counts",
"V2Themes",
"V2Locations",
"V2Persons",
"V2Organizations",
"V2Tone",
"Amounts")

filtered_df.write.mode('overwrite').parquet("hdfs:///user/hajili/data_frame_gkg_2.parquet")
