# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import os
import django
import django_endesive

DEBUG = True
USE_TZ = True

# TEMPORARY ROOT FOR TEST FILES
TEMP_ROOT = '{}/temp/'.format(os.path.dirname(django_endesive.__file__))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "3k-sq=x8cp(4av04b9&7uhu=0w!@b-@o)*6*v+dm+21!r3yxcf"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}


INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_endesive",
]

# DJANGO ENDESIVE SETTINGS
DJANGO_ENDESIVE = {
    'PDF_CERTIFICATE_PATH': TEMP_ROOT+'demo2_user1.p12',
    'PDF_CERTIFICATE_PASSWORD': '1234',
    'PDF_ATTRIBUTES': {
        'CONTACT': 'you@example.com',
        'LOCATION': 'United States',
        'REASON': 'Signing motivation'
    }
}

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
