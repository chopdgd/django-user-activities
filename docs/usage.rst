=====
Usage
=====

To use django-user-activities in a project, add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'user_activities.apps.UserActivitiesConfig',
        ...
    )

Add django-user-activities's URL patterns:

.. code-block:: python

    from user_activities import urls as user_activities_urls


    urlpatterns = [
        ...
        url(r'^', include(user_activities_urls)),
        ...
    ]
