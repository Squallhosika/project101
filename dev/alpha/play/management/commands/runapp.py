import sys
import os

from play.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        # parser.add_argument('-u', action='user', user=self.run_app('user'))
        # parser.add_argument('-c', action='client', user=self.run_app('client'))
        parser.add_argument(
            '-s',
            dest='service',
            default='all',
            help='Run the specified service.',
        )
        # parser.add_argument(
        #     '--u', action='store_true', dest='user', default=False,
        #     help='Run the specified service.',
        # )
        # parser.add_argument(
        #     '-c', dest='client',
        #     help='Run the specified service.',
        # )

    def handle(self, *args, **options):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

        self.app = str(options['service'])

        return self.run_app()

    def run_app(self):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'
        UNIC_ROOT = os.environ['UNIC_ROOT']

        if self.app == 'all':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\external\userApp_GUI.py'
            cmd2 = 'start cmd /k ' + UNIC_ROOT + r'\external\clientApp_GUI.py'

            os.system(str(cmd1))
            os.system(str(cmd2))

        elif self.app == 'user':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\external\userApp_GUI.py'
            os.system(str(cmd1))

        elif self.app == 'client':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\external\clientApp_GUI.py'
            os.system(str(cmd1))

        # sys.stdout.write(app)
        # c = os.system(str(cmd1))
        sys.stdout.write(self.app)