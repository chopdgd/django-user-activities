# -*- coding: utf-8 -*-
import django_filters
from genomix.filters import DisplayChoiceFilter

from . import choices, models


class ActivityFilter(django_filters.rest_framework.FilterSet):

    username = django_filters.CharFilter(
        name='user__username',
        lookup_expr='iexact',
    )
    activity_type = DisplayChoiceFilter(choices=choices.ACTIVITY_TYPES)

    class Meta:
        model = models.Activity
        fields = [
            'user',
            'activity_type',
            'active',
            'content_type',
            'object_id',
        ]


class CommentFilter(django_filters.rest_framework.FilterSet):

    username = django_filters.CharFilter(
        name='user__username',
        lookup_expr='iexact',
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Tag.objects.all(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.Comment
        fields = [
            'user',
            'active',
            'tags',
            'content_type',
            'object_id',
        ]


class ReviewFilter(django_filters.rest_framework.FilterSet):

    username = django_filters.CharFilter(
        name='user__username',
        lookup_expr='iexact',
    )
    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Tag.objects.all(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.Review
        fields = [
            'user',
            'active',
            'tags',
            'content_type',
            'object_id',
            'rating',
        ]
