from kafka import KafkaProducer
from kafka.errors import KafkaError


class KProducer():

    def __init__(self):
        self.kafka_host = 'localhost'
        self.kafka_port = '9092'
        self.kafka_topics = ['test']
        self.kafka_groups = ['group-1']

        self.producer = KafkaProducer(bootstrap_servers=[self.kafka_host + ':' + self.kafka_port])

    def startThread(self):
        pass

    def start(self):
        pass

if __name__ == '__main__':

    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])

    # Asynchronous by default
    future = producer.send('test', b'raw_bytes')

    # Block for 'synchronous' sends
    try:
        record_metadata = future.get(timeout=10)
    except KafkaError:
        # Decide what to do if produce request failed...
        # log.exception()
        pass

    # Successful result returns assigned partition and offset
    print (record_metadata.topic)
    print (record_metadata.partition)
    print (record_metadata.offset)

    # produce keyed messages to enable hashed partitioning
    producer.send('test', key=b'foo', value=b'bar')

    # encode objects via msgpack
    # producer = KafkaProducer(value_serializer=msgpack.dumps)
    # producer.send('msgpack-topic', {'key': 'value'})

    # produce json messages
    # producer = KafkaProducer(value_serializer=lambda m: json.dumps(m).encode('ascii'))
    # producer.send('json-topic', {'key': 'value'})
    #
    # # produce asynchronously
    # for _ in range(100):
    #     producer.send('my-topic', b'msg')
    #
    # # block until all async messages are sent
    # producer.flush()
    #
    # # configure multiple retries
    # producer = KafkaProducer(retries=5)