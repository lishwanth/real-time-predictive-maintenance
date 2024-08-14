from kafka import KafkaConsumer
import json
from config.kafka_config import KafkaConfig

class KafkaDataConsumer:
    def __init__(self):
        self.consumer = KafkaConsumer(
            KafkaConfig.TOPIC,
            bootstrap_servers=KafkaConfig.BOOTSTRAP_SERVERS,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            group_id='maintenance-group'
        )

    def consume_data(self):
        for message in self.consumer:
            data = json.loads(message.value.decode('utf-8'))
            print(f"Consumed data: {data}")
            # Process the data here

if __name__ == "__main__":
    consumer = KafkaDataConsumer()
    consumer.consume_data()
