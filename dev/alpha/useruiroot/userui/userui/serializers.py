from userui.userui.models import *


@classmethod
def from_json(cls, json_string):
    json_dic = json.loads(json_string)
    event.event_type = json_dic['event_type']
    for key, value in json_dic.items():
        if key in event.__dict__:
            event.__dict__[key] = value

    return event


def to_json(self):
    json_string = '{'
    for key, value in self.__dict__.items():
        json_string += '"{}":"{}",'.format(key, value)
    json_string = json_string[:(len(json_string) - 1)]
    json_string += '}'
    return json_string

