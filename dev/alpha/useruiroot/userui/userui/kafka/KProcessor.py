import json
from userui.userui.kafka.KProducer import KProducer


class KProcessor:

    def __init__(self, event_to_fct):
        self.event_to_fct = event_to_fct
        pass

    def process(self, msg):
        msg_value = msg.value.decode("utf-8")
        event = KEvent.from_json(msg_value)
        self.event_to_fct[event.broker_topic][event.event_name](event.body)


class KGenerator:

    def __init__(self):
        self.kproducer = KProducer()

    def publish(self, event):
        json_string = event.to_json()
        return self.kproducer.send(event.broker_topic, json_string)


class KEvent:

    def __init__(self, sender="userui", broker_topic="order", event_type="w",
                 event_name=None, body=None):
        self.sender = sender
        self.broker_topic = broker_topic
        self.event_type = event_type
        self.event_name = event_name
        self.body = body

    def __str__(self):
        return self.body

    def event_name(self, event_name):
        self.event_name = event_name
        return self

    def event_type(self, event_type):
        self.event_type = event_type
        return self

    def body(self, body):
        self.body = body
        return self

    @classmethod
    def from_json(cls, json_string):
        event = KEvent()
        json_dic = json.loads(json_string)
        event.event_type = json_dic['event_type']
        # TODO smarter way like the constructor
        # ...
        return event

    def to_json(self):
        json_string = '{'
        for key, value in self.__dict__.items():
            json_string += '"{}":"{}",'.format(key, value)
        json_string = json_string[:(len(json_string)-1)]
        json_string += '}'
        return json_string


if __name__ == '__main__':

    generator = KGenerator()
    # event0 = KEvent(event_name='create_order', body='thisIsABody')
    # generator.publish(event=event0)


# https://codecanyon.net/item/material-design-ui-android-template-app/9858746

# http://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html
# https://www.confluent.io/blog/making-sense-of-stream-processing/

# {
#     "sender": "userui",
#     "brokerTopic": "order",
#     "eventType": "write",
#     "action": "create_order", #(eventType)
#     "body":
#     {
#
#     }
# }