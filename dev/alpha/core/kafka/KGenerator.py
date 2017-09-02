from core.kafka.KProducer import KProducer
from core.kafka.KEvent import KEvent

import inspect

class KGenerator:

    def __init__(self, settings):
        self.settings = settings
        self.fct_to_event = self.settings.FCT_TO_EVENT
        self.kproducer = KProducer(settings)


    def generate(self, event_body):
        event = self.serializeEvent(event_body)
        json_string = event.to_json()
        return self.kproducer.send(event.broker_topic, json_string)

    def serializeEvent(self, event_body):
        ct = inspect.stack()[3]
        # for c in ct:
        #     print(c)
        print(ct.function)

        if ct.function in self.fct_to_event.keys():
            print(True)
            # event_name = 'create_order'
            # event_topic = 'order'
            params = self.fct_to_event[ct.function]
            event = KEvent(**params)
            print(event.event_name)
        else:
            print(False)

        # @ TODO based on caller
        event_name = 'test'
        event_topic = 'test'
        return KEvent(broker_topic=event_topic, event_name=event_name, body=event_body)

#
#
# if __name__ == '__main__':
#     generator = KGenerator()
#     event0 = KEvent(event_name='create_order', body='thisIsABody')
#     generator.publish(event=event0)