"""
Kafka Consumer module
"""
from kafka import KafkaConsumer
import json


class KafkaConsumerClient:
    """
    Handles consuming messages from a Kafka topic.
    """
    def __init__(self, bootstrap_servers: str, topic: str):
        self.bootstrap_servers = bootstrap_servers
        self.topic = topic
        self.consumer = KafkaConsumer(
            self.topic,
            bootstrap_servers=self.bootstrap_servers,
            value_deserializer=lambda x: json.loads(x.decode("utf-8")),  # Deserialize JSON
            auto_offset_reset="earliest",
            enable_auto_commit=True,
        )

    def get_message_by_value(self, key: str, value: str):
        """
        Searches for a message with the specified value in the topic.
        Assumes messages are JSON-encoded and structured as dictionaries containing a <key> field.
        TODO: implement timeout
        :return: The message (as a dictionary) if found, else None.
        """
        # Poll all messages from the topic
        for message in self.consumer:
            if message.value.get(key) == value:
                print(f"[KafkaConsumer] Found message: {message.value}")
                return message.value  # Return the matching message

        print(f"[KafkaConsumer] Message with field: {key} and value: '{value}' not found.")
        return None