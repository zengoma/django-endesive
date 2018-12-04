=====
Usage
=====

To use Django Endesive in a project, add it to your `INSTALLED_APPS`:

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
