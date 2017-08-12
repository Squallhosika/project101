

class KProcessor():

    def __init__(self):
        pass

    @staticmethod
    def process(msg):
        print(msg.value)

    def parseEvent(self, event):
        pass


class KGenerator():

    def __init__(self):
        pass




class KEvent():

    def __init__(self):
        self.sender = "userui"
        self.broker_topic = "order"
        self.event_type = "w"


    def setTargetTopic(self, topic):
        self.target_topic = topic



# https://codecanyon.net/item/material-design-ui-android-template-app/9858746

# http://docs.aws.amazon.com/step-functions/latest/dg/concepts-amazon-states-language.html
# https://www.confluent.io/blog/making-sense-of-stream-processing/

{
    "sender": "userui",
    "brokerTopic": "order",
    "eventType": "write",
    "action": "create_order", #(eventType)
    "body":
    {

    }
}