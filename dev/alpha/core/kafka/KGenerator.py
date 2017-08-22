from core.kafka.KProducer import KProducer
from core.kafka.KEvent import KEvent

class KGenerator:

    def __init__(self, settings):
        self.fct_to_event = settings.FCT_TO_EVENT
        self.kproducer = KProducer(settings)


    def generate(self, event_body):
        event = self.wrapEvent(event_body)
        json_string = event.to_json()
        return self.kproducer.send(event.broker_topic, json_string)

    def wrapEvent(self, event_body):
        # @ TODO based on caller
        event_name = 'create_order'
        event_topic = 'order'
        return KEvent(broker_topic=event_topic, event_name=event_name, body=event_body)



if __name__ == '__main__':
    generator = KGenerator()
    event0 = KEvent(event_name='create_order', body='thisIsABody')
    generator.publish(event=event0)