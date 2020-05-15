"""
WSGI config for WSB_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WSB_website.settings')

application = get_wsgi_application()

from whitenoise.django import DjangoWhiteNoise
<<<<<<< HEAD
application = DjangoWhiteNoise(application)
=======
application = DjangoWhiteNoise(application)
>>>>>>> 960f9a1... This is a test commit with deployment preparations
