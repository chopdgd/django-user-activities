# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from user_activities.urls import urlpatterns as user_activities_urls

urlpatterns = [
    url(r'^', include(user_activities_urls, namespace='user_activities')),
]
