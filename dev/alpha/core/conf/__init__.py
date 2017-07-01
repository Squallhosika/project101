import importlib


class Settings():
    def __init__(self):
        self.SETTINGS_MODULE = "core.conf.settings"
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

# settings = Settings()

if __name__ == '__main__':
    # pass
    # print('test')
    settings = Settings()
    print(settings.SERVICES)