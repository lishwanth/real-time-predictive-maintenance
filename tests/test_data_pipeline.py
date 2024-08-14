import unittest
from data_pipeline.kafka_producer import KafkaDataProducer

class TestKafkaProducer(unittest.TestCase):
    def test_produce_data(self):
        producer = KafkaDataProducer()
        self.assertIsNotNone(producer.produce_data({"test": "data"}))

if __name__ == "__main__":
    unittest.main()