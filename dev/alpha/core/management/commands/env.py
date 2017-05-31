import sys
import os

from core.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'
        return self.run_env()

    def run_env(self):
        UNIC_ROOT = os.environ['UNIC_ROOT']
        cmd1 = 'start cmd /k ' + UNIC_ROOT + '\env\Scripts\activate.bat'
        os.system(str(cmd1))
        sys.stdout.write(self.service)