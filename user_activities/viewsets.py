# -*- coding: utf-8 -*-
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets

from . import filters, models, serializers


class ActivityViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing User Activities."""

    queryset = models.Activity.objects.fast()
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = filters.ActivityFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return serializers.ActivitySerializerCreateOrEdit
        return serializers.ActivitySerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing User Comments."""

    queryset = models.Comment.objects.fast()
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = filters.CommentFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return serializers.CommentSerializerCreateOrEdit
        return serializers.CommentSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    """ViewSet for viewing and editing User Reviews."""

    queryset = models.Review.objects.fast()
    permission_classes = (permissions.IsAuthenticated, )
    filter_backends = (DjangoFilterBackend, )
    filterset_class = filters.ReviewFilter

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PUT', 'PATCH']:
            return serializers.ReviewSerializerCreateOrEdit
        return serializers.ReviewSerializer
