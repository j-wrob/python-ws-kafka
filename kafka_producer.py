"""
Kafka Producer module
"""
from kafka import KafkaProducer
import json


class KafkaProducerClient:
    """
    Handles producing messages to a Kafka topic.
    """
    def __init__(self, bootstrap_servers, topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.producer = KafkaProducer(
            bootstrap_servers=self.bootstrap_servers,
            value_serializer=lambda v: json.dumps(v).encode('utf-8')  # Serialize message as JSON
        )

    def send(self, data):
        """
        Sends data to the Kafka topic.
        """
        print(f"[KafkaProducer] Sending message to topic '{self.topic}': {data}")
        future = self.producer.send(self.topic, value=data)
        result = future.get()  # Wait for Kafka's confirmation
        return result

    def close(self):
        """
        Closes the Kafka producer.
        """
        self.producer.close()