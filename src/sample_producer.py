import sys
from argparse import ArgumentParser
from threading import Timer
from time import time
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
from random import randint
from sample_source_props import random_movie, random_email_addr, random_tags, random_sentence


class PeriodicProducer(object):
    def __init__(self, bootstrap_servers, schema_registry_url, topic):
        value_schema = avro.load('resources/workshop.avsc')
        config = {
            'bootstrap.servers': bootstrap_servers,
            'schema.registry.url': 'http://{0}'.format(schema_registry_url)
        }
        self.topic = topic
        self.stopped = True
        self.end_time = 0
        self.producer = AvroProducer(config, default_value_schema=value_schema)

    def __loop__(self):
        now = int(time())
        document = {
            'timestamp': now,
            'email': random_email_addr(),
            'movie': random_movie(),
            'tags': random_tags(),
            'comment': random_sentence(),
            'rating': randint(0, 9)
        }
        print 'Sending {0} to kafka.'.format(document)
        self.producer.produce(topic=self.topic, value=document)

        if not self.stopped and now < self.end_time:
            Timer(1, self.__loop__).start()

    def run(self, period):
        self.stopped = False
        self.end_time = int(time()) + period
        self.__loop__()

    def is_stopped(self):
        return self.stopped

    def is_running(self):
        return not self.stopped

    def stop(self):
        self.stopped = True


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--brokers', help='kafka brokers list')
    parser.add_argument('--schema-registry', dest='schema_registry', help='schema registry url')
    parser.add_argument('--topic', help='target kafka topic')

    args = parser.parse_args(sys.argv[1:])

    producer = PeriodicProducer(args.brokers, args.schema_registry, args.topic)
    producer.run(60)
