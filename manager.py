#!/usr/bin/env python
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def init_django():
    import django
    from django.conf import settings

    if settings.configured:
        return

    settings.configure(
        INSTALLED_APPS=[
            'app',
        ],
        DATABASES={
            'default': {
                'ENGINE': 'django.db.backends.mysql',
                'NAME': 'db_default',
                'USER': 'root',
                'PASSWORD': 'root',
                'HOST': '127.0.0.1',
                'PORT': '3306',
            },
        },
        DEFAULT_AUTO_FIELD='django.db.models.BigAutoField',

    )
    django.setup()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    init_django()
    execute_from_command_line()
