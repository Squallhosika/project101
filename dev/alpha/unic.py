#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # os.environ.setdefault("DJANGO_SETTINGS_MODULE", "env")
    # sys.path.append(os.getcwd() + 'play\\')

    try:
        from play.management import execute_from_command_line
    except ImportError:
        try:
            import play.management
        except ImportError:
            # sys.stdout.write(os.getcwd())
            raise ImportError(
                "Couldn't import Unic. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)