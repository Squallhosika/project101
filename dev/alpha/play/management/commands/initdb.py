import sys
import os

from play.management.base import BaseCommand, CommandError

class Command(BaseCommand):
    help = (
        "Fills the service database using the csv files."
        "(using each model's default manager unless --all is specified)."
    )

    def add_arguments(self, parser):
        parser.add_argument(
                '-s', '--service',
                dest='service',
                default='all',
                # action='store_true',
                help='Run the specified service.')

        parser.add_argument(
                '-t', '--table',
                dest='table',
                default='all',
                # action='store_true',
                help='Run the specified service.')

        parser.add_argument(
                '-f', '--flush',
                dest='flush',
                default=True,
                action='store_true',
                help='Run the specified service.')

        parser.add_argument(
                '-nf', '--no-flush',
                dest='flush',
                default=False,
                action='store_false',
                help='Run the specified service.')


    def handle(self, *args, **options):

        os.environ['UNIC_ROOT'] = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

        self.service = options['service']
        self.table = options['table']
        self.flush = options['flush']

        return self.run_app()


    def run_app(self):
        UNIC_ROOT = os.environ['UNIC_ROOT']

        if self.service == 'client':
            if self.flush:
                cmd0 = UNIC_ROOT + r'\clientroot\manage.py flush'
                os.system(str(cmd0))

            if self.table == 'all':
                cmd = UNIC_ROOT + r'\play\setup_dbs.py -s ' + str(self.service)
            else:
                cmd = UNIC_ROOT + r'\play\setup_dbs.py -s ' + str(self.service) + ' -t ' + str(self.table)

        if self.service == 'order':
            cmd = 'start cmd /k ' + UNIC_ROOT + r'\play\setup_dbs.py order'

        os.system(str(cmd))
        # sys.stdout.write(app)