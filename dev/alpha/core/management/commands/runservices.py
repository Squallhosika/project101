import sys
import os
import webbrowser

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

        parser.add_argument(
                '-w', '--web',
                dest='web',
                default=False,
                action='store_true',
                help='Run the specified service.')

        parser.add_argument(
            '-n', '--network-type',
            dest='network-type',
            default='local',
            help='Select the network type.')

    def handle(self, *args, **options):
        self.service = options['service']
        self.web = options['web']
        self.network_type = options['network-type']

        return self.run_services()

    def run_services(self):

        settings = conf.Settings()
        os.environ['PYTHONPATH'] = settings.UNIC_ROOT

        UNIC_ROOT = settings.UNIC_ROOT
        services = settings.SERVICES

        cmds = []
        for service, params in services.items():
            host = params['URLS'][self.network_type]['HOST']
            port = params['URLS'][self.network_type]['PORT']
            root = params['ROOT']
            cmd = params['CMD']

            if service == self.service or self.service == 'all':
                cmd = 'start cmd /k python ' + UNIC_ROOT + root + cmd + ' ' + host + ':' + port
                cmds.append(cmd)

        for cmd in cmds:
            os.system(str(cmd))

        if self.web:
            for _, params in services.items():
                host = params['HOST']
                port = params['PORT']
                webbrowser.open('http://' + host + ':' + port)

        sys.stdout.write(self.service + ' service started')
