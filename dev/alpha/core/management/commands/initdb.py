import sys
import os

from core.management.base import BaseCommand, CommandError
import core.conf as conf

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

        self.service = options['service']
        self.table = options['table']
        self.flush = options['flush']

        return self.run_app()

    def run_app(self):

        settings = conf.Settings()

        UNIC_ROOT = settings.UNIC_ROOT
        databases = settings.DATABASES

        flush_cmd = databases['CMD']['FLUSH_CMD']         #'\manage.py flush'
        save_cmd = databases['CMD']['SAVE_CMD']
        services = databases['SERVICES']
        update_all = databases['UPDATE_ALL']

        cmds = ['set PYTHONPATH=' + settings.UNIC_ROOT]
        if self.service == 'all':
            for service_name, update in update_all.items():
                if update:
                    if service_name in services:
                        service_root = services[service_name]['SERVICE_ROOT']

                        if self.flush:
                            cmd0 = 'python ' + UNIC_ROOT + service_root + flush_cmd
                            cmds.append(cmd0)

                        cmd1 = 'python ' + UNIC_ROOT + save_cmd + ' -s ' + str(service_name)
                        if self.table != 'all':
                            cmd1 = cmd1 + ' -t ' + str(self.table)

                        cmds.append(cmd1)

                    else:
                        print(service_name + ' service in update all but not in conf')
                else:
                    print(service_name + 'not set to update in conf ALL')

        else:
            if self.service in services:
                service_root = services[self.service]['SERVICE_ROOT']
                if self.flush:
                    cmd0 = 'python ' + UNIC_ROOT + service_root + flush_cmd
                    cmds.append(cmd0)

                cmd1 = 'python ' + UNIC_ROOT + save_cmd + ' -s ' + str(self.service)
                if self.table != 'all':
                    cmd1 = cmd1 + ' -t ' + str(self.table)

                cmds.append(cmd1)
            else:
                print('service not in conf')


        for cmd in cmds:
            os.system(str(cmd))

        sys.stdout.write(self.service + ' db reset')