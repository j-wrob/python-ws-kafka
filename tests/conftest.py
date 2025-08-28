# import pytest
# import subprocess
# import time

# Kafka and Zookeeper Configuration TODO: Should go to config file
# ZOOKEEPER_PORT = 2181
# KAFKA_PORT = 9092
# KAFKA_BOOTSTRAP_SERVERS = f"localhost:{KAFKA_PORT}"
# TOPIC_NAME = "sample_topic"
# WEBSOCKET_URL = "wss://ws.postman-echo.com/raw"


# @pytest.fixture(scope="module", autouse=True)
# def start_kafka_services():
#     """
#     Start Zookeeper and Kafka locally as part of the test setup.
#     """
#     # Start Zookeeper
#     print("[SETUP] Starting Zookeeper...")
#     zookeeper = subprocess.Popen([
#         "./zookeeper-server-start.sh", "../config/zookeeper.properties"
#     ], cwd="kafka/bin")
#     time.sleep(15)  # Allow Zookeeper to initialize
#
#     # Start Kafka Broker
#     print("[SETUP] Starting Kafka Broker...")
#     kafka_broker = subprocess.Popen([
#         "./kafka-server-start.sh", "../config/server.properties"
#     ], cwd="kafka/bin")
#     time.sleep(15)  # Allow Kafka broker to initialize
#
#     # Create Kafka topic
#     print(f"[SETUP] Creating Kafka topic '{TOPIC_NAME}'...")
#     subprocess.run([
#         "./kafka-topics.sh", "--create",
#         "--topic", TOPIC_NAME,
#         "--bootstrap-server", KAFKA_BOOTSTRAP_SERVERS,
#         "--partitions", "1", "--replication-factor", "1"
#     ], cwd="kafka/bin")
#     time.sleep(10)
#
#     # Yield control to the tests
#     yield
#
#     # Teardown: Stop Kafka and Zookeeper
#     print("[TEARDOWN] Stopping Kafka and Zookeeper...")
#     kafka_broker.terminate()
#     zookeeper.terminate()
