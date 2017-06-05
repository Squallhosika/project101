import os
import sys
from argparse import ArgumentParser

# from django.utils.encoding import force_str
# from django.core.management.color import color_style, no_style
# from django.core import checks


class CommandError(Exception):
    """
    Exception class indicating a problem while executing a management
    command.

    If this exception is raised during the execution of a management
    command, it will be caught and turned into a nicely-printed error
    message to the appropriate output stream (i.e., stderr); as a
    result, raising this exception (with a sensible description of the
    error) is the preferred way to indicate that something has gone
    wrong in the execution of a command.
    """
    pass

class SystemCheckError(CommandError):
    """
    The system check framework detected unrecoverable errors.
    """
    pass


class CommandParser(ArgumentParser):
    """
    Customized ArgumentParser class to improve some error messages and prevent
    SystemExit in several occasions, as SystemExit is unacceptable when a
    command is called programmatically.
    """
    def __init__(self, cmd, **kwargs):
        self.cmd = cmd
        super(CommandParser, self).__init__(**kwargs)

    def parse_args(self, args=None, namespace=None):
        # Catch missing argument for a better error message
        if (hasattr(self.cmd, 'missing_args_message') and
                not (args or any(not arg.startswith('-') for arg in args))):
            self.error(self.cmd.missing_args_message)
        return super(CommandParser, self).parse_args(args, namespace)

    def error(self, message):
        if self.cmd._called_from_command_line:
            super(CommandParser, self).error(message)
        else:
            raise CommandError("Error: %s" % message)

def handle_default_options(options):
    """
    Include any default options that all commands should accept here
    so that ManagementUtility can handle them before searching for
    user commands.
    """
    pass
    # if options.settings:
    #     os.environ['UNIC_SETTINGS_MODULE'] = options.settings
    # if options.pythonpath:
    #     sys.path.insert(0, options.pythonpath)


class BaseCommand(object):
    """
    The base class from which all management commands ultimately
    derive.

    Use this class if you want access to all of the mechanisms which
    parse the command-line arguments and work out what code to call in
    response; if you don't need to change any of that behavior,
    consider using one of the subclasses defined in this file.

    If you are interested in overriding/customizing various aspects of
    the command-parsing and -execution behavior, the normal flow works
    as follows:

    1. ``django-admin`` or ``manage.py`` loads the command class
       and calls its ``run_from_argv()`` method.

    2. The ``run_from_argv()`` method calls ``create_parser()`` to get
       an ``ArgumentParser`` for the arguments, parses them, performs
       any environment changes requested by options like
       ``pythonpath``, and then calls the ``execute()`` method,
       passing the parsed arguments.

    3. The ``execute()`` method attempts to carry out the command by
       calling the ``handle()`` method with the parsed arguments; any
       output produced by ``handle()`` will be printed to standard
       output and, if the command is intended to produce a block of
       SQL statements, will be wrapped in ``BEGIN`` and ``COMMIT``.

    4. If ``handle()`` or ``execute()`` raised any exception (e.g.
       ``CommandError``), ``run_from_argv()`` will  instead print an error
       message to ``stderr``.

    Thus, the ``handle()`` method is typically the starting point for
    subclasses; many built-in commands and command types either place
    all of their logic in ``handle()``, or perform some additional
    parsing work in ``handle()`` and then delegate from it to more
    specialized methods as needed.

    Several attributes affect behavior at various steps along the way:

    ``can_import_settings``
        A boolean indicating whether the command needs to be able to
        import Django settings; if ``True``, ``execute()`` will verify
        that this is possible before proceeding. Default value is
        ``True``.

    ``help``
        A short description of the command, which will be printed in
        help messages.

    ``output_transaction``
        A boolean indicating whether the command outputs SQL
        statements; if ``True``, the output will automatically be
        wrapped with ``BEGIN;`` and ``COMMIT;``. Default value is
        ``False``.

    ``requires_migrations_checks``
        A boolean; if ``True``, the command prints a warning if the set of
        migrations on disk don't match the migrations in the database.

    ``requires_system_checks``
        A boolean; if ``True``, entire Django project will be checked for errors
        prior to executing the command. Default value is ``True``.
        To validate an individual application's models
        rather than all applications' models, call
        ``self.check(app_configs)`` from ``handle()``, where ``app_configs``
        is the list of application's configuration provided by the
        app registry.

    ``leave_locale_alone``
        A boolean indicating whether the locale set in settings should be
        preserved during the execution of the command instead of translations
        being deactivated.

        Default value is ``False``.

        Make sure you know what you are doing if you decide to change the value
        of this option in your custom command if it creates database content
        that is locale-sensitive and such content shouldn't contain any
        translations (like it happens e.g. with django.contrib.auth
        permissions) as activating any locale might cause unintended effects.

        This option can't be False when the can_import_settings option is set
        to False too because attempting to deactivate translations needs access
        to settings. This condition will generate a CommandError.
    """
    # Metadata about this command.
    help = ''
    _called_from_command_line = False


    def __init__(self, stdout=None, stderr=None, no_color=False):
        self.stdout = stdout or sys.stdout
        self.stderr = stderr or sys.stderr
        # if no_color:
        #     self.style = no_style()
        # else:
        #     self.style = color_style()
        #     self.stderr.style_func = self.style.ERROR

    def get_version(self):
        """
        Return the Django version, which should be correct for all built-in
        Django commands. User-supplied commands can override this method to
        return their own version.
        """
        return str(1.0)

    def create_parser(self, prog_name, subcommand):
        """
        Create and return the ``ArgumentParser`` which will be used to
        parse the arguments to this command.
        """
        parser = CommandParser(
            self, prog="%s %s" % (os.path.basename(prog_name), subcommand),
            description=self.help or None,
        )
        parser.add_argument('--version', action='version', version=self.get_version())

        self.add_arguments(parser)
        return parser

    def add_arguments(self, parser):
        """
        Entry point for subclassed commands to add custom arguments.
        """
        pass

    def print_help(self, prog_name, subcommand):
        """
        Print the help message for this command, derived from
        ``self.usage()``.
        """
        parser = self.create_parser(prog_name, subcommand)
        parser.print_help()

    def run_from_argv(self, argv):
        """
        Set up any environment changes requested (e.g., Python path
        and Django settings), then run this command. If the
        command raises a ``CommandError``, intercept it and print it sensibly
        to stderr. If the ``--traceback`` option is present or the raised
        ``Exception`` is not ``CommandError``, raise it.
        """
        self._called_from_command_line = True
        parser = self.create_parser(argv[0], argv[1])

        options = parser.parse_args(argv[2:])
        cmd_options = vars(options)
        # Move positional args out of options to mimic legacy optparse
        args = cmd_options.pop('args', ())
        handle_default_options(options)
        try:
            self.execute(*args, **cmd_options)
        except Exception as e:
            # if options.traceback or not isinstance(e, CommandError):
            #     raise

            # SystemCheckError takes care of its own formatting.
            # if isinstance(e, SystemCheckError):
            #     self.stderr.write(str(e), lambda x: x)
            # else:
            #     self.stderr.write('%s: %s' % (e.__class__.__name__, e))
            sys.exit(1)
        finally:
            pass
            # connections.close_all()

    def execute(self, *args, **options):
        """
        Try to execute this command, performing system checks if needed (as
        controlled by the ``requires_system_checks`` attribute, except if
        force-skipped).
        """
        output = self.handle(*args, **options)
        return output

    def handle(self, *args, **options):
        """
        The actual logic of the command. Subclasses must implement
        this method.
        """
        raise NotImplementedError('subclasses of BaseCommand must provide a handle() method')
