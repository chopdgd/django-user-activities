# -*- coding: utf-8 -*-
from django.db.models import CharField

import django_filters
from genomix.filters import DisplayChoiceFilter

from . import choices, models


class ActivityFilter(django_filters.rest_framework.FilterSet):

    activity_type = DisplayChoiceFilter(choices=choices.ACTIVITY_TYPES)

    class Meta:
        model = models.Activity
        fields = [
            'user',
            'user__username',
            'activity_type',
            'active',
            'content_type',
            'content_type__model',
            'object_id',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'iexact',
                },
            }
        }


class CommentFilter(django_filters.rest_framework.FilterSet):

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Tag.objects.all(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.Comment
        fields = [
            'user',
            'user__username',
            'active',
            'tags',
            'tags__label',
            'content_type',
            'content_type__model',
            'object_id',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'iexact',
                },
            }
        }


class ReviewFilter(django_filters.rest_framework.FilterSet):

    tags = django_filters.ModelMultipleChoiceFilter(
        queryset=models.Tag.objects.all(),
        widget=django_filters.widgets.CSVWidget,
        help_text='Multiple values may be separated by commas.',
    )

    class Meta:
        model = models.Review
        fields = [
            'user',
            'user__username',
            'active',
            'tags',
            'tags__label',
            'content_type',
            'content_type__model',
            'object_id',
            'rating',
            'rating__label',
        ]
        filter_overrides = {
            CharField: {
                'filter_class': django_filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'iexact',
                },
            }
        }
