FROM ubuntu:16.10

RUN apt-get update && \
    apt-get -y install python python-pip python-dev gcc librdkafka-dev librdkafka++1 && \
    pip install avro requests confluent-kafka

ENV KAFKA=localhost:9092 \
    SCHEMA_REGISTRY=localhost:8081 \
    TOPIC=workshop

ADD src/*.py /producer/
ADD resources/workshop.avsc /producer/resources/

WORKDIR /producer
CMD python sample_producer.py --brokers $KAFKA --schema-registry $SCHEMA_REGISTRY --topic $TOPIC