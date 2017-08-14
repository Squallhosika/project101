
class KSettings:
    def __init__(self, event_to_fct, host, port, topics, groups):
        self.event_to_fct = event_to_fct
        self.kafka_host = host
        self.kafka_port = port
        self.kafka_topics = topics
        self.kafka_groups = groups


