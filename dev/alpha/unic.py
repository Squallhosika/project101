#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("UNIC_SETTINGS_MODULE", "core.conf")
    sys.path.extend(['C:\\Users\\Jonathan\\git\\unicorn\\dev\\alpha'])

    try:
        from core.management import execute_from_command_line
    except ImportError:
        try:
            import core
        except ImportError:
            raise ImportError(
                "Couldn't import Unic. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)