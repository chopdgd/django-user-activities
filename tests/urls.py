# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^', include('user_activities.urls', namespace='user_activities')),
    url(r'^admin/', admin.site.urls),
]
