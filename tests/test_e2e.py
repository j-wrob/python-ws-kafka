"""
E2E test for ws-kafka interface
"""
import pytest

from ws_kafka_interface import WebSocketKafkaInterface
from kafka_consumer import KafkaConsumerClient

# Kafka and Zookeeper Configuration
ZOOKEEPER_PORT = 2181
KAFKA_PORT = 9092
KAFKA_BOOTSTRAP_SERVERS = f"localhost:{KAFKA_PORT}"
TOPIC_NAME = "sample_topic"
WEBSOCKET_URL = "wss://ws.postman-echo.com/raw"

@pytest.mark.asyncio
async def test_ws_to_kafka_e2e():
    """
    Test the end-to-end flow:
    - Send a message via WebSocket
    - Verify the response is sent and consumed by Kafka
    """
    # Initialize WebSocket-Kafka interface
    interface = WebSocketKafkaInterface(
        WEBSOCKET_URL,
        KAFKA_BOOTSTRAP_SERVERS,
        TOPIC_NAME
    )

    # Test WebSocket message
    test_message = "E2E test message"
    await interface.process_ws_to_kafka(test_message)

    # Kafka Consumer: Listen for the message
    consumer_client = KafkaConsumerClient(KAFKA_BOOTSTRAP_SERVERS, TOPIC_NAME)

    # Consume messages from Kafka and verify the sent one
    print("[TEST] Verifying message in Kafka...")
    for message in consumer_client.consumer:  # Use the existing consumer loop
        kafka_data = message.value
        assert kafka_data["websocket_sent"] == test_message, "Kafka message does not match sent WebSocket message!"
        assert kafka_data["websocket_received"] == test_message, "Kafka message does not match received WebSocket response!"
        print("[TEST] Successfully verified Kafka message:", kafka_data)
        break  # Stop after the first verified message

