"""
Kafka Consumer module
"""
from kafka import KafkaConsumer
import json


class KafkaConsumerClient:
    """
    Handles consuming messages from a Kafka topic.
    """
    def __init__(self, bootstrap_servers, topic):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),  # Deserialize JSON
            auto_offset_reset="earliest",
            enable_auto_commit=True
        )

    def consume(self):
        """
        Listen for messages from the Kafka topic.
        """
        print(f"[KafkaConsumer] Listening for messages on topic '{self.topic}'...")
        for message in self.consumer:
            print(f"[KafkaConsumer] Received message: {message.value}")