from ws_client import WebSocketClient
from kafka_producer import KafkaProducerClient


class WebSocketKafkaInterface:
    """
    Interface class that connects WebSocket client and Kafka producer.
    1. Fetch message from WebSocket.
    2. Send the received message to Kafka.
    """
    def __init__(self, websocket_url, kafka_bootstrap_servers, kafka_topic):
        self.websocket_client = WebSocketClient(websocket_url)
        self.kafka_producer = KafkaProducerClient(kafka_bootstrap_servers, kafka_topic)

    async def process_ws_to_kafka(self, message):
        """
        Send WebSocket message, fetch the response, and forward it to Kafka.
        :param message: Message to send through WebSocket.
        """
        try:
            # 1. Send WebSocket message and get response
            ws_sent, ws_received = await self.websocket_client.send_message(message)

            # 2. Format the message and send it to Kafka
            kafka_message = {
                "websocket_sent": ws_sent,
                "websocket_received": ws_received
            }
            self.kafka_producer.send(kafka_message)
            print(f"WebSocket response forwarded to Kafka: {kafka_message}")

        finally:
            # Ensure Kafka producer is properly closed
            self.kafka_producer.close()