=============================
Django Endesive
=============================

.. image:: https://badge.fury.io/py/django-endesive.svg
    :target: https://badge.fury.io/py/django-endesive

.. image:: https://travis-ci.org/zengoma/django-endesive.svg?branch=master
    :target: https://travis-ci.org/zengoma/django-endesive

.. image:: https://codecov.io/gh/zengoma/django-endesive/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/zengoma/django-endesive

Django endesive PDF digital signing utility.

Documentation
-------------

The full documentation is at https://django-endesive.readthedocs.io.

Quickstart
----------

Install Django Endesive::

    pip install django-endesive

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_endesive.apps.DjangoEndesiveConfig',
        ...
    )

Add Django Endesive's URL patterns:

.. code-block:: python

    from django_endesive import urls as django_endesive_urls


    urlpatterns = [
        ...
        url(r'^', include(django_endesive_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_
*  Endesive_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
.. _Endesive: https://github.com/m32/endesive/blob/master/examples/pdf-sign-cms.py
