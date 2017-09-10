import json


class KEvent:

    def __init__(self, sender=None, broker_topic=None, event_type=None,
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

    def event_topic(self, broker_topic):
        self.broker_topic = broker_topic
        return self


    @classmethod
    def from_json(cls, json_string):
        event = KEvent()
        json_dic = json.loads(json_string)
        for key, value in json_dic.items():
            if key in event.__dict__:
                event.__dict__[key] = value

        return event

    def to_json(self):
        json_string = '{'
        for key, value in self.__dict__.items():
            json_string += '"{}":"{}",'.format(key, value)
        json_string = json_string[:(len(json_string)-1)]
        json_string += '}'
        return json_string
