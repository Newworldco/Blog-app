"""
WSGI config for django_pjct project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""
import sys
import os
from django.core.wsgi import get_wsgi_application

path = "/home/Invictuss/django_pjct"
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'django_pjct.settings'

application = get_wsgi_application()
