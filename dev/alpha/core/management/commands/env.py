import sys
import os
import core.conf.settings as settings

from core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        os.environ['UNIC_ROOT'] = settings.UNIC_ROOT
        return self.run_env()

    def run_env(self):
        UNIC_ROOT = os.environ['UNIC_ROOT']
        cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\env\Scripts\activate.bat'
        os.system(str(cmd1))
        sys.stdout.write(self.service)
