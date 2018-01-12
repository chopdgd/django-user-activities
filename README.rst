=============================
Django User Activities
=============================

.. image:: https://badge.fury.io/py/django-user-activities.svg
    :target: https://badge.fury.io/py/django-user-activities

.. image:: https://travis-ci.org/chopdgd/django-user-activities.svg?branch=develop
    :target: https://travis-ci.org/chopdgd/django-user-activities

.. image:: https://codecov.io/gh/chopdgd/django-user-activities/branch/develop/graph/badge.svg
    :target: https://codecov.io/gh/chopdgd/django-user-activities

.. image:: https://pyup.io/repos/github/chopdgd/django-user-activities/shield.svg
    :target: https://pyup.io/repos/github/chopdgd/django-user-activities/
    :alt: Updates

.. image:: https://pyup.io/repos/github/chopdgd/django-user-activities/python-3-shield.svg
    :target: https://pyup.io/repos/github/chopdgd/django-user-activities/
    :alt: Python 3

Django app for dealing with User activities (likes, tags, comments, etc.)

Documentation
-------------

The full documentation is at https://django-user-activities.readthedocs.io.

Quickstart
----------

Install Django User Activities::

    pip install django-user-activities

Add it to your `INSTALLED_APPS` (along with DRF and django-filters):

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'rest_framework',
        'django_filters',
        ...
        'user_activities',
        ...
    )

Add Django User Activities's URL patterns:

.. code-block:: python

    from user_activities import urls as user_activities_urls


    urlpatterns = [
        ...
        url(r'^', include(user_activities_urls, namespace='user_activities')),
        ...
    ]

Using Activity, Comment, or Review in your models:

.. code-block:: python

    from django.contrib.contenttypes.fields import GenericRelation
    from django.db import models


    class ExampleModel(models.Model):
        ...
        comments = GenericRelation('user_activities.Comment')
        user_activities = GenericRelation('user_activities.Activity')

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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
