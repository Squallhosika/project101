import sys
import os

from play.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        parser.add_argument(
            '-s', dest='service',
            help='Run the specified service.',
        )

    def handle(self, *args, **options):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'
        self.service = 'all'
        if options['service']:
            self.service = str(options['service'])

        return self.run_services()

    def run_services(self):
        UNIC_ROOT = os.environ['UNIC_ROOT']
        cmd1 = 'start cmd /k ' + UNIC_ROOT + '\clientroot\manage.py runserver 127.0.0.1:8000'
        cmd2 = 'start cmd /k ' + UNIC_ROOT + '\orderroot\manage.py runserver 127.0.0.1:8001'
        os.system(str(cmd1))
        # os.system(str(cmd2))
        sys.stdout.write(self.service)
