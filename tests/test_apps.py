from django.apps import apps
from django.test import TestCase
from django_endesive.apps import DjangoEndesiveConfig


class DjangoEndesiveConfigTest(TestCase):
    def test_apps(self):
        self.assertEqual(DjangoEndesiveConfig.name, 'django_endesive')
        self.assertEqual(apps.get_app_config('django_endesive').name, 'django_endesive')
