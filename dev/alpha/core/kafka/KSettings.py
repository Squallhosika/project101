import importlib
import inspect


class KSettings:
    def __init__(self, service): #, settings_module): #, event_to_fct, fct_to_event, host, port, topics, groups):
        # self.event_to_fct = event_to_fct
        # self.fct_to_event = fct_to_event
        # self.kafka_host = host
        # self.kafka_port = port
        # self.kafka_topics = topics
        # self.kafka_groups = groups


        self.SETTINGS_MODULE = self.getSettingsModule(service) #"core.conf.settings"
        self._configured = None

        mod = importlib.import_module(self.SETTINGS_MODULE)

        for setting in dir(mod):
            if setting.isupper():
                setting_value = getattr(mod, setting)
                setattr(self, setting, setting_value)
                self._configured = True

    @property
    def configured(self):
        return self._configured is not None

    def getSettingsModule(self, service):
        #return 'clientuiroot.clientui.clientui.kafka.kafka_settings'
        # ct = inspect.stack()[3]
        # print(ct.filename)

        return service + 'root.' + service + '.' + service + '.kafka.ksettings'

        # if service == 'clientui':
        #     return 'clientuiroot.clientui.clientui.kafka.kafka_settings'
        # else:
        #     return 'clientuiroot.clientui.clientui.kafka.kafka_settings'




if __name__ == '__main__':

    ksettings = KSettings('clientui')
    print(ksettings.BROKER['HOST'])
    # print(ksettings)
