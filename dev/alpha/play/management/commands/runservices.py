import sys
import os
import webbrowser

from play.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            dest='service',
            default='all',
            help='Run the specified service.',
        )

        parser.add_argument(
                '-w', '--web',
                dest='web',
                default=False,
                action='store_true',
                help='Run the specified service.')

    def handle(self, *args, **options):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

        self.service = options['service']
        self.web = options['web']

        return self.run_services()

    def run_services(self):
        UNIC_ROOT = os.environ['UNIC_ROOT']
        # cmd1 = 'start cmd /k ' + UNIC_ROOT + '\clientroot\manage.py runserver 127.0.0.1:8000'
        # cmd2 = 'start cmd /k ' + UNIC_ROOT + '\orderroot\manage.py runserver 127.0.0.1:8003'

        if self.service == 'all':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + '\clientroot\manage.py runserver 127.0.0.1:8000'
            cmd2 = 'start cmd /k ' + UNIC_ROOT + '\orderroot\manage.py runserver 127.0.0.1:8003'

            os.system(str(cmd1))
            os.system(str(cmd2))

            if self.web:
                webbrowser.open('http://127.0.0.1:8000')
                webbrowser.open('http://127.0.0.1:8003')

        elif self.service == 'client':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + '\clientroot\manage.py runserver 127.0.0.1:8000'
            os.system(str(cmd1))

            if self.web:
                webbrowser.open('http://127.0.0.1:8000')


        elif self.service == 'order':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + '\orderroot\manage.py runserver 127.0.0.1:8003'
            os.system(str(cmd1))

            if self.web:
                webbrowser.open('http://127.0.0.1:8003')


        # os.system(str(cmd1))
        # os.system(str(cmd2))
        sys.stdout.write(self.service)
