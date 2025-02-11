from pyspark.sql import SparkSession
from pyspark.sql.functions import udf
from pyspark.sql.types import DoubleType

# Initialize Spark Session
spark = SparkSession.builder.appName("UDF Example").getOrCreate()

# Sample data
data = [("USD", 100), ("EUR", 80), ("JPY", 9800)]
columns = ["Currency", "Amount"]

# Create DataFrame
df = spark.createDataFrame(data, columns)

# Define UDF for currency conversion (simplified)
def convert_to_usd(currency, amount):
    conversion_rates = {"USD": 1, "EUR": 1.1, "JPY": 0.009}
    return amount * conversion_rates.get(currency, 1)

# Register UDF
usd_conversion_udf = udf(convert_to_usd, DoubleType())

# Apply UDF
converted_df = df.withColumn("AmountInUSD", usd_conversion_udf(df.Currency, df.Amount))

converted_df.show()