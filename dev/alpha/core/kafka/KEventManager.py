from core.kafka.KGenerator import KGenerator
from core.kafka.KConsumer import KConsumer


class KEventManager:

    def __init__(self, settings):
        self.settings = settings
        self.kgenerator = KGenerator(settings)
        self.kconsumer = KConsumer(settings)

    def start(self):
        self.kconsumer.start()
