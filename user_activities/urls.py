# -*- coding: utf-8 -*-
from rest_framework import routers

from . import viewsets


app_name = 'user_activities'
router = routers.SimpleRouter()
router.register(r'', viewsets.ActivityViewSet)
router.register(r'comments', viewsets.CommentViewSet)
router.register(r'reviews', viewsets.ReviewViewSet)

default_router = routers.DefaultRouter()
default_router.register(r'user-activities', viewsets.ActivityViewSet)
default_router.register(r'comments', viewsets.CommentViewSet)
default_router.register(r'reviews', viewsets.ReviewViewSet)

urlpatterns = default_router.urls
