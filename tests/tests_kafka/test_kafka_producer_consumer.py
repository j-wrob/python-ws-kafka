import time
from kafka_consumer import KafkaConsumerClient
from kafka_producer import KafkaProducerClient

# Kafka Configuration TODO: should go to config file
KAFKA_PORT = 9092
KAFKA_BOOTSTRAP_SERVERS = f"localhost:{KAFKA_PORT}"
TOPIC_NAME = "timestamped_topic"

def test_kafka_producer_consumer():
    """
    Test kafka broker by sending message from producer and receiving it by consumer
    """
    producer_client = KafkaProducerClient(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, topic=TOPIC_NAME)
    consumer_client = KafkaConsumerClient(bootstrap_servers=KAFKA_BOOTSTRAP_SERVERS, topic=TOPIC_NAME)

    timestamp = str(time.time())
    producer_client.send(data={
        "timestamp": timestamp,
        "message_text": "sample text"})

    message = consumer_client.get_message_by_value(key="timestamp", value=timestamp)
    assert message["message_text"] == "sample text"

    producer_client.close()