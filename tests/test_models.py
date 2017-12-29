#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` models module.
"""

import pytest

from .fixtures import (
    Activity,
    Comment,
    Review,
    Rating,
    Tag,
)


@pytest.mark.django_db
class TestActivity(object):

    def test_str(self, Activity):
        assert str(Activity) == 'favorite'

    def test_attributes(self, Activity):
        assert Activity.user.username == 'username'
        assert Activity.activity_type == 0
        assert Activity.get_activity_type_display() == 'favorite'
        assert Activity.content_type.model == 'comment'
        assert Activity.object_id == 1


@pytest.mark.django_db
class TestRating(object):

    def test_str(self, Rating):
        assert str(Rating) == 'label'

    def test_attributes(self, Rating):
        assert Rating.label == 'label'
        assert Rating.description == 'description'


@pytest.mark.django_db
class TestTag(object):

    def test_str(self, Tag):
        assert str(Tag) == 'tag'

    def test_attributes(self, Tag):
        assert Tag.label == 'tag'
        assert Tag.description == 'description'


@pytest.mark.django_db
class TestComment(object):

    def test_str(self, Comment):
        assert str(Comment) == 'text'

    def test_attributes(self, Comment):
        assert Comment.user.username == 'username'
        assert Comment.text == 'text'
        assert Comment.active is True
        assert Comment.activities.all()[0].id == 1
        assert Comment.content_type.model == 'comment'
        assert Comment.object_id == 1


@pytest.mark.django_db
class TestReview(object):

    def test_str(self, Review):
        assert str(Review) == 'text'

    def test_attributes(self, Review):
        assert Review.user.username == 'username'
        assert Review.text == 'text'
        assert Review.active is True
        assert Review.activities.all()[0].id == 1
        assert str(Review.rating) == 'label'
        assert Review.content_type.model == 'review'
        assert Review.object_id == 1
