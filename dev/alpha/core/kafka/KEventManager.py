from core.kafka.KConsumer import KConsumer
from core.kafka.KProducer import KProducer

from core.kafka.KProcessor import KProcessor
from core.kafka.KGenerator import KGenerator

from core.kafka.KSettings import KSettings

import inspect


class KEventManager:

    def __init__(self, service): #, settings):
        # self.settings = settings
        self.ksettings = KSettings(service)

        self.kconsumer = KConsumer(self.ksettings)
        # self.kprocessor = self.kconsumer.kprocessor

        self.kproducer = KProducer(self.ksettings)
        self.kgenerator = KGenerator(self.ksettings)

    def start(self):
        # self.kconsumer.start()
        self.kconsumer.startThread()


    def publish(self, event_body):
        # event = KEvent(event_name='create_order', body='thisIsABody')
        self.kgenerator.generate(event_body)

    def subscribe(self):
        pass



if __name__ == '__main__':
    # ksettings = KSettings('geo')
    # cons = KConsumer(ksettings)
    # prod = KProducer(ksettings)

    # prod.send('test', '{"name":"test"}')


    em = KEventManager('geo')
    em.publish('tessssss')
    em.start()

    # cons.startThread()