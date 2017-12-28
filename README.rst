=============================
Django User Activities
=============================

.. image:: https://badge.fury.io/py/django-user-activities.svg
    :target: https://badge.fury.io/py/django-user-activities

.. image:: https://travis-ci.org/genomics-geek/django-user-activities.svg?branch=master
    :target: https://travis-ci.org/genomics-geek/django-user-activities

.. image:: https://codecov.io/gh/genomics-geek/django-user-activities/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/genomics-geek/django-user-activities

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

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'user_activities.apps.UserActivitiesConfig',
        ...
    )

Add Django User Activities's URL patterns:

.. code-block:: python

    from user_activities import urls as user_activities_urls


    urlpatterns = [
        ...
        url(r'^', include(user_activities_urls)),
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

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
