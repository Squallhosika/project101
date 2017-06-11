import sys
import os

from core.management.base import BaseCommand, CommandError
import core.conf as conf

class Command(BaseCommand):
    help = "Runs all services in local servers based on config file"

    def add_arguments(self, parser):
        parser.add_argument(
            '-s',
            dest='service',
            default='all',
            help='Run the specified service.',
        )

    def handle(self, *args, **options):
        # os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

        self.app = str(options['service'])

        return self.run_app()

    def run_app(self):
        # pass
        settings = conf.Settings()

        UNIC_ROOT = settings.UNIC_ROOT
        apps = settings.APPS

        cmds = []
        for app, params in apps.items():
            root = params['ROOT']
            gui = params['GUI']

            if app == self.app or self.app == 'all':
                cmd = 'start cmd /k python ' + UNIC_ROOT + root + gui
                cmds.append(cmd)

        for cmd in cmds:
            os.system(str(cmd))


        sys.stdout.write(self.app + ' app started')

        # UNIC_ROOT = os.environ['UNIC_ROOT']
        #
        # if self.app == 'all':
        #     cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\core\app\gui\userApp_GUI.py'
        #     cmd2 = 'start cmd /k ' + UNIC_ROOT + r'\core\app\gui\clientApp_GUI.py'
        #
        #     os.system(str(cmd1))
        #     os.system(str(cmd2))
        #
        # elif self.app == 'user':
        #     cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\core\app\gui\userApp_GUI.py'
        #     os.system(str(cmd1))
        #
        # elif self.app == 'client':
        #     cmd1 = 'start cmd /k ' + UNIC_ROOT + r'\core\app\gui\clientApp_GUI.py'
        #     os.system(str(cmd1))
        #
        # # sys.stdout.write(app)
        # # c = os.system(str(cmd1))
        # sys.stdout.write(self.app)