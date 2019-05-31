#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` models module.
"""

import pytest

from .fixtures import *  # NOQA


@pytest.mark.django_db
def test_Activity(Activity):
    instance = Activity(activity_type=0, object_id=20)
    assert str(instance) == 'favorite'


@pytest.mark.django_db
def test_Rating(Rating):
    instance = Rating(label='rating', description='desc')
    assert str(instance) == 'rating'


@pytest.mark.django_db
def test_Tag(Tag):
    instance = Tag(label='tag', description='desc')
    assert str(instance) == 'tag'


@pytest.mark.django_db
def test_Comment(Comment):
    instance = Comment(text='comment')
    assert str(instance) == 'comment'


@pytest.mark.django_db
def test_Review(Review):
    instance = Review(text='comment')
    assert str(instance) == 'comment'
