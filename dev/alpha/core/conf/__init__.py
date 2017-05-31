import sys
import os
# sys.path.extend(['C:\\Users\\Keuvin\\Documents\\Unicorn\\GIT\\unicorn_master\\dev\\alpha'])
# os.environ.setdefault("UNIC_SETTINGS_MODULE", "core.conf.settings")

import importlib


# ENVIRONMENT_VARIABLE = "UNIC_SETTINGS_MODULE"


class Settings():
    def __init__(self):
        sys.path.extend(['C:\\Users\\Keuvin\\Documents\\Unicorn\\GIT\\unicorn_master\\dev\\alpha'])
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