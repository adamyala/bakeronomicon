#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import json
import os
import sys


def main():
    print("trying to load localhost env vars")
    with open("localhost-environment-variables.json") as file:
        secrets = json.load(file)

    for key, value in secrets.items():
        if not value:
            # if any value is falsey, the file is empty
            local_vars_loaded = False
            break
        os.environ.setdefault(key, value)
        local_vars_loaded = True

    if local_vars_loaded:
        print("localhost env vars loaded")
    else:
        print("did not load vars. not on localhost")

    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bakeronomicon.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
