# -*- coding: utf-8
from django.contrib.contenttypes.models import ContentType

from model_mommy import mommy
import pytest


@pytest.fixture
def User():
    def _func(username='username', **kwargs):
        return mommy.make('auth.User', username=username, **kwargs)
    return _func


@pytest.fixture
def Activity():
    def _func(content_type=None, user=None, **kwargs):
        if not content_type:
            content_type = ContentType.objects.get(model='comment')
        if not user:
            user = mommy.make('auth.User', username='username')

        return mommy.make(
            'user_activities.Activity',
            content_type=content_type,
            user=user,
            **kwargs
        )
    return _func


@pytest.fixture
def Rating():
    def _func(**kwargs):
        return mommy.make('user_activities.Rating', **kwargs)
    return _func


@pytest.fixture
def Tag():
    def _func(**kwargs):
        return mommy.make('user_activities.Tag', **kwargs)
    return _func


@pytest.fixture
def Comment():
    def _func(content_type=None, user=None, **kwargs):
        if not content_type:
            content_type = ContentType.objects.get(model='comment')
        if not user:
            user = mommy.make('auth.User', username='username')

        return mommy.make(
            'user_activities.Comment',
            content_type=content_type,
            user=user,
            **kwargs
        )
    return _func


@pytest.fixture
def Review():
    def _func(content_type=None, user=None, rating=None, **kwargs):
        if not content_type:
            content_type = ContentType.objects.get(model='comment')
        if not user:
            user = mommy.make('auth.User', username='username')

        return mommy.make(
            'user_activities.Review',
            rating=rating,
            content_type=content_type,
            user=user,
            **kwargs
        )
    return _func
