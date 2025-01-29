from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Initialize Spark session
spark = SparkSession.builder.master("local").appName("Data Cleaning") \
    .getOrCreate()

# Sample data
data = [("Harry", "Gryffindor", "Friendly"),
        ("Tom", "Slytherin", "Evil"),
        ("Luna", "Ravenclaw", "Friendly"),
        ("Draco", "Slytherin", "Friendly")]

# Create DataFrame
columns = ["Name", "House", "Nature"]
df = spark.createDataFrame(data, columns)

# Filter only friendly creatures
friendly_df = df.filter(col("Nature") == "Friendly").select("Name", "House")

# Show result
friendly_df.show()