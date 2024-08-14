from kafka import KafkaProducer
import json
from config.kafka_config import KafkaConfig
import time

class KafkaDataProducer:
    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=KafkaConfig.BOOTSTRAP_SERVERS)
    
    def produce_data(self, data):
        self.producer.send(KafkaConfig.TOPIC, json.dumps(data).encode('utf-8'))
        self.producer.flush()

if __name__ == "__main__":
    producer = KafkaDataProducer()
    
    sample_data = {
        "timestamp": time.time(),
        "sensor_1": 30.5,
        "sensor_2": 45.2,
        "sensor_3": 60.1,
        "status": "normal"
    }
    
    producer.produce_data(sample_data)
    print("Data sent to Kafka")
