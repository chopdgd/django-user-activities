# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include
from django.contrib import admin

from user_activities.urls import urlpatterns as user_activities_urls


app_name = 'user_activities'
urlpatterns = [
    url(r'^', include(user_activities_urls)),
    url(r'^admin/', admin.site.urls),
]
