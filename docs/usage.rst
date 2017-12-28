=====
Usage
=====

To use Django User Activities in a project, add it to your `INSTALLED_APPS`:

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
