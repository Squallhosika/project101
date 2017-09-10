from core.kafka.KEvent import KEvent


class KProcessor:

    def __init__(self, settings):
        self.settings = settings
        self.event_to_fct = self.settings.EVENT_TO_FCT
        pass

    def process(self, json_string):
        # msg_value = msg.value.decode("utf-8")
        event = self.deserializeEvent(json_string)
        if event.event_name in self.event_to_fct[event.broker_topic]:
            self.event_to_fct[event.broker_topic][event.event_name](event.body)

    def deserializeEvent(self, json_string):
        return KEvent.from_json(json_string)


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