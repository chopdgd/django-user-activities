#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` models module.
"""
from django.test import TestCase

from . import fixtures


class TestActivity(TestCase):

    def setUp(self):
        self.instance = fixtures.Activity()

    def test_str(self):
        assert str(self.instance) == 'favorite'

    def test_attributes(self):
        assert self.instance.user.username == 'username'
        assert self.instance.activity_type == 0
        assert self.instance.get_activity_type_display() == 'favorite'
        assert self.instance.content_type.model == 'comment'
        assert self.instance.object_id == 1


class TestRating(TestCase):

    def setUp(self):
        self.instance = fixtures.Rating()

    def test_str(self):
        assert str(self.instance) == 'label'

    def test_attributes(self):
        assert self.instance.label == 'label'
        assert self.instance.description == 'description'


class TestTag(TestCase):

    def setUp(self):
        self.instance = fixtures.Tag()

    def test_str(self):
        assert str(self.instance) == 'tag'

    def test_attributes(self):
        assert self.instance.label == 'tag'
        assert self.instance.description == 'description'


class TestComment(TestCase):

    def setUp(self):
        self.instance = fixtures.Comment()

    def test_str(self):
        assert str(self.instance) == 'text'

    def test_attributes(self):
        assert self.instance.user.username == 'username'
        assert self.instance.text == 'text'
        assert self.instance.active is True
        assert self.instance.activities.all()[0].id == 1
        assert self.instance.content_type.model == 'comment'
        assert self.instance.object_id == 1


class TestReview(TestCase):

    def setUp(self):
        self.instance = fixtures.Review()

    def test_str(self):
        assert str(self.instance) == 'text'

    def test_attributes(self):
        assert self.instance.user.username == 'username'
        assert self.instance.text == 'text'
        assert self.instance.active is True
        assert self.instance.activities.all()[0].id == 1
        assert str(self.instance.rating) == 'label'
        assert self.instance.content_type.model == 'review'
        assert self.instance.object_id == 1
