# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.utils.text import slugify

import django_filters

from . import models


class CommentFilter(django_filters.rest_framework.FilterSet):

    username = django_filters.CharFilter(
        method='filter_username',
        label='Username',
    )
    content_model = django_filters.CharFilter(
        method='filter_content_model',
        label='ContentType Model',
    )

    class Meta:
        model = models.Comment
        fields = [
            'user',
            'active',
            'content_type',
            'object_id',
        ]

    def filter_username(self, queryset, name, value):
        return queryset.filter(Q(user__username__iexact=value))

    def filter_content_model(self, queryset, name, value):
        obj = ContentType.objects.get(model=value.replace(" ", "").lower())
        return queryset.filter(Q(content_type=obj.id))


class ReviewFilter(django_filters.rest_framework.FilterSet):

    username = django_filters.CharFilter(
        method='filter_username',
        label='Username',
    )
    content_model = django_filters.CharFilter(
        method='filter_content_model',
        label='ContentType Model',
    )
    rating_label = django_filters.CharFilter(
        method='filter_rating_label',
        label='Rating Label',
    )

    class Meta:
        model = models.Review
        fields = [
            'user',
            'active',
            'content_type',
            'object_id',
            'rating',
        ]

    def filter_username(self, queryset, name, value):
        return queryset.filter(Q(user__username__iexact=value))

    def filter_content_model(self, queryset, name, value):
        obj = ContentType.objects.get(model=value.replace(" ", "").lower())
        return queryset.filter(Q(content_type=obj.id))

    def filter_rating_label(self, queryset, name, value):
        return queryset.filter(Q(rating__slug=slugify(value)))
