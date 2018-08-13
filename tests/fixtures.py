# -*- coding: utf-8
from django.contrib.contenttypes.models import ContentType

from model_mommy import mommy
import pytest


@pytest.fixture
def Activity(content_type='comment'):

    return mommy.make(
        'user_activities.Activity',
        id=1,
        user=mommy.make('auth.User', id=1, username='username'),
        activity_type=0,
        content_type=ContentType.objects.get(model=content_type),
        object_id=1,
    )


@pytest.fixture
def Rating():

    return mommy.make(
        'user_activities.Rating',
        id=1,
        label='label',
        description='description',
    )


@pytest.fixture
def Tag():

    return mommy.make(
        'user_activities.Tag',
        id=1,
        label='tag',
        description='description',
    )


@pytest.fixture
def Comment():

    Activity(content_type='comment')

    return mommy.make(
        'user_activities.Comment',
        id=1,
        user=mommy.make('auth.User', id=1, username='username'),
        text='text',
        active=True,
        content_type=ContentType.objects.get(model='comment'),
        object_id=1,
    )


@pytest.fixture
def Review():

    Activity(content_type='review')

    return mommy.make(
        'user_activities.Review',
        id=1,
        user=mommy.make('auth.User', id=1, username='username'),
        text='text',
        active=True,
        rating=Rating(),
        content_type=ContentType.objects.get(model='review'),
        object_id=1,
    )
