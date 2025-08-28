# python-ws-kafka
Simple implementation of message flow from websocket to kafka consumer

- Prior to run tests it is required to:

- start zookeeper:
>./zookeeper-server-start.sh ../config/zookeeper.properties

- start kafka broker:
>./kafka-server-start.sh ../config/server.properties

- create kafka topic:
>./kafka-topics.sh --create --topic sample_topic --bootstrap-server localhost:9092 --partitions 1 --replication-factor 1

- verify by listing topics:
>./kafka-topics.sh --list --bootstrap-server localhost:9092