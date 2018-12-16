import os
from pyspark.sql import *
from pyspark.sql.functions import unix_timestamp, udf, to_date
from pyspark.sql.types import *
from datetime import datetime
spark = SparkSession.builder.getOrCreate()
spark.conf.set('spark.sql.session.timeZone', 'UTC')
sc = spark.sparkContext

DATA_DIR='hdfs:///datasets/gdeltv2/'

MENTIONS_SCHEMA = StructType([
    StructField("GLOBALEVENTID_MENTIONS",LongType(),True),
    StructField("EventTimeDate_MENTIONS",LongType(),True),
    StructField("MentionTimeDate_MENTIONS",LongType(),True),
    StructField("MentionType_MENTIONS",LongType(),True),
    StructField("MentionSourceName_MENTIONS",StringType(),True),
    StructField("MentionIdentifier_MENTIONS",StringType(),True),
    StructField("SentenceID_MENTIONS",LongType(),True),
    StructField("Actor1CharOffset_MENTIONS",LongType(),True),
    StructField("Actor2CharOffset_MENTIONS",LongType(),True),
    StructField("ActionCharOffset_MENTIONS",LongType(),True),
    StructField("InRawText_MENTIONS",LongType(),True),
    StructField("Confidence_MENTIONS",LongType(),True),
    StructField("MentionDocLen_MENTIONS",LongType(),True),
    StructField("MentionDocTone_MENTIONS",FloatType(),True),
    StructField("MentionDocTranslationInfo_MENTIONS",StringType(),True),
    StructField("Extras_MENTIONS",StringType(),True)
    ])





mentions=spark.read.csv(schema=MENTIONS_SCHEMA,path=os.path.join(DATA_DIR, "*.mentions.CSV"), sep="\t")

EVENTS_SCHEMA = StructType([
    StructField("GLOBALEVENTID",LongType(),True),
    StructField("Day_DATE",StringType(),True),
    StructField("MonthYear_Date",StringType(),True),
    StructField("Year_Date",StringType(),True),
    StructField("FractionDate",FloatType(),True),
    StructField("Actor1Code",StringType(),True),
    StructField("Actor1Name",StringType(),True),
    StructField("Actor1CountryCode",StringType(),True),
    StructField("Actor1KnownGroupCode",StringType(),True),
    StructField("Actor1EthnicCode",StringType(),True),
    StructField("Actor1Religion1Code",StringType(),True),
    StructField("Actor1Religion2Code",StringType(),True),
    StructField("Actor1Type1Code",StringType(),True),
    StructField("Actor1Type2Code",StringType(),True),
    StructField("Actor1Type3Code",StringType(),True),
    StructField("Actor2Code",StringType(),True),
    StructField("Actor2Name",StringType(),True),
    StructField("Actor2CountryCode",StringType(),True),
    StructField("Actor2KnownGroupCode",StringType(),True),
    StructField("Actor2EthnicCode",StringType(),True),
    StructField("Actor2Religion1Code",StringType(),True),
    StructField("Actor2Religion2Code",StringType(),True),
    StructField("Actor2Type1Code",StringType(),True),
    StructField("Actor2Type2Code",StringType(),True),
    StructField("Actor2Type3Code",StringType(),True),
    StructField("IsRootEvent",LongType(),True),
    StructField("EventCode",StringType(),True),
    StructField("EventBaseCode",StringType(),True),
    StructField("EventRootCode",StringType(),True),
    StructField("QuadClass",LongType(),True),
    StructField("GoldsteinScale",FloatType(),True),
    StructField("NumMentions",LongType(),True),
    StructField("NumSources",LongType(),True),
    StructField("NumArticles",LongType(),True),
    StructField("AvgTone",FloatType(),True),
    StructField("Actor1Geo_Type",LongType(),True),
    StructField("Actor1Geo_FullName",StringType(),True),
    StructField("Actor1Geo_CountryCode",StringType(),True),
    StructField("Actor1Geo_ADM1Code",StringType(),True),
    StructField("Actor1Geo_ADM2Code",StringType(),True),
    StructField("Actor1Geo_Lat",FloatType(),True),
    StructField("Actor1Geo_Long",FloatType(),True),
    StructField("Actor1Geo_FeatureID",StringType(),True),
    StructField("Actor2Geo_Type",LongType(),True),
    StructField("Actor2Geo_FullName",StringType(),True),
    StructField("Actor2Geo_CountryCode",StringType(),True),
    StructField("Actor2Geo_ADM1Code",StringType(),True),
    StructField("Actor2Geo_ADM2Code",StringType(),True),
    StructField("Actor2Geo_Lat",FloatType(),True),
    StructField("Actor2Geo_Long",FloatType(),True),
    StructField("Actor2Geo_FeatureID",StringType(),True),
    StructField("ActionGeo_Type",LongType(),True),
    StructField("ActionGeo_FullName",StringType(),True),
    StructField("ActionGeo_CountryCode",StringType(),True),
    StructField("ActionGeo_ADM1Code",StringType(),True),
    StructField("ActionGeo_ADM2Code",StringType(),True),
    StructField("ActionGeo_Lat",FloatType(),True),
    StructField("ActionGeo_Long",FloatType(),True),
    StructField("ActionGeo_FeatureID",StringType(),True),
    StructField("DATEADDED",LongType(),True),
    StructField("SOURCEURL",StringType(),True)
    ])


DATA_DIR="hdfs:///datasets/gdeltv2"
spark_df = spark.read.option("delimiter", "\t").csv(schema=EVENTS_SCHEMA, path=os.path.join(DATA_DIR, "*.export.CSV"))


filtered_df = spark_df.filter( ( spark_df["Actor1Name"].contains("REFUGEE") ) | (spark_df["Actor2Name"].contains("REFUGEE") ) )


joined = filtered_df.join(mentions, filtered_df.GLOBALEVENTID == mentions.GLOBALEVENTID_MENTIONS) 

joined.write.mode('overwrite').parquet("hdfs:///user/karalupo/joined.parquet")