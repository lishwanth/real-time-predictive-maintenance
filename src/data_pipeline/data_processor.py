from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from config.spark_config import SparkConfig

class DataProcessor:
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName(SparkConfig.APP_NAME) \
            .master(SparkConfig.MASTER) \
            .getOrCreate()

    def process_data(self, data_path):
        df = self.spark.read.csv(data_path, header=True, inferSchema=True)
        df = df.withColumn("sensor_1_normalized", col("sensor_1") / 100)
        df.show()

if __name__ == "__main__":
    processor = DataProcessor()
    processor.process_data("datasets/turbofan/train_FD001.txt")
