from core.kafka.KProducer import KProducer

class KGenerator:

    def __init__(self, settings):
        self.kproducer = KProducer(settings)

    def publish(self, event):
        json_string = event.to_json()
        return self.kproducer.send(event.broker_topic, json_string)

if __name__ == '__main__':
    generator = KGenerator()
    event0 = KEvent(event_name='create_order', body='thisIsABody')
    generator.publish(event=event0)