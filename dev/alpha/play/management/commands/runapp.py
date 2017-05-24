import sys
import os

from play.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        parser.add_argument('-u', action='user', user=self.run_app('user'))
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
        self.app = 'all'
        if options['user']:
            self.app = 'user'

        return self.run_app(self.app)

    def run_app(self, app):
        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'
        UNIC_ROOT = os.environ['UNIC_ROOT']
        if app == 'user':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\external\userApp_GUI.py'
        elif app == 'client':
            cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\external\userApp_GUI.py'

        # sys.stdout.write(app)
        c = os.system(str(cmd1))
        sys.stdout.write(app)