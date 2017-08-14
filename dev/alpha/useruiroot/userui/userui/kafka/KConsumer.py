from kafka import KafkaConsumer, TopicPartition
from useruiroot.userui.userui.kafka.KProcessor import KProcessor


class KConsumer:

    def __init__(self):
        self.kafka_host = 'localhost'
        self.kafka_port = '9092'
        self.kafka_topics = ['order']
        self.kafka_groups = ['group-1']

        # self.client = kafka.SimpleClient(self.kafka_host + ':' + self.kafka_port)
        # self.consumer = kafka.SimpleConsumer(self.client, self.kafka_groups[0], self.kafka_topics[0])

        self.consumer = KafkaConsumer(bootstrap_servers=[self.kafka_host + ':' + self.kafka_port])

    def startThread(self):
        pass

    def start_old(self):
        # TODO here only the first topic is selected
        partition = TopicPartition(self.kafka_topics[0], 0)

        self.consumer.assign([partition])
        self.consumer.seek_to_beginning(partition)

        for msg in self.consumer:
            print(msg[6])
            # KProcessor.process(msg)

    def start(self):
        partitions = [TopicPartition(x, 0) for x in self.kafka_topics]
        self.consumer.assign(partitions)
        self.consumer.seek_to_beginning(partitions[0])

        while True:
            msg = next(self.consumer)
            print(msg[6])
            # use KProducer here

    def close(self):
        self.consumer.close()

    def add_topics(self, topics):
        self.kafka_topics.append(topics)

    def remove_topics(self, topics):
        self.kafka_topics.remove(topics)

if __name__ == '__main__':

    consumer = KConsumer()
    consumer.start()
    consumer.close()

    # client = kafka.SimpleClient('localhost:9092')
    # consumer = kafka.SimpleConsumer(client, "group1", "test")

    # for message in consumer:
    #     print('test')
    #     print(message.message.value)


    # consumer = KafkaConsumer('test',
    #                          group_id='group2',
    #                          bootstrap_servers='127.0.0.1:9092')
    #                          # bootstrap_servers='localhost:9092')
    # # partition = TopicPartition('test', 1)
    # # consumer.assign(partition)
    # # records = consumer.seek_to_beginning()
    # m = consumer.poll(100)
    # m = consumer.seek_to_beginning()
    # for message in consumer:
    #     # message value and key are raw bytes -- decode if necessary!
    #     # e.g., for unicode: `message.value.decode('utf-8')`
    #     print ("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
    #                                       message.offset, message.key,
    #                                       message.value))

# consume earliest available messages, don't commit offsets
# KafkaConsumer(auto_offset_reset='earliest', enable_auto_commit=False)
#
# # consume json messages
# KafkaConsumer(value_deserializer=lambda m: json.loads(m.decode('ascii')))
#
# # consume msgpack
# KafkaConsumer(value_deserializer=msgpack.unpackb)
#
# # StopIteration if no message after 1sec
# KafkaConsumer(consumer_timeout_ms=1000)
#
# # Subscribe to a regex topic pattern
# consumer = KafkaConsumer()
# consumer.subscribe(pattern='^awesome.*')
#
# # Use multiple consumers in parallel w/ 0.9 kafka brokers
# # typically you would run each on a different server / process / CPU
# consumer1 = KafkaConsumer('my-topic',
#                           group_id='my-group',
#                           bootstrap_servers='my.server.com')
# consumer2 = KafkaConsumer('my-topic',
#                           group_id='my-group',
#                           bootstrap_servers='my.server.com')