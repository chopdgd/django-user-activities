#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` fields module.
"""

from django.test import TestCase
from mock import MagicMock
import pytest

from user_activities import fields

from . import fixtures


def RatingRelatedField():
    return fields.RatingRelatedField(read_only=True)


def TagRelatedField():
    return fields.TagRelatedField(read_only=True)


class FieldTestCase(TestCase):
    field = None

    def test_to_representation(self):
        if self.field:
            assert self.field.to_representation(self.internal_value) == self.display_value

    def test_to_representation_failure(self):
        if self.field:
            with pytest.raises(Exception):
                self.field.to_representation(self.bad_internal_value)

    def test_to_internal_value(self):
        if self.field:
            assert self.field.to_internal_value(self.display_value) == self.internal_value

    def test_to_internal_value_failure(self):
        if self.field:
            with pytest.raises(Exception):
                self.field.to_internal_value(self.bad_display_value)


class TestRatingRelatedField(FieldTestCase):

    def setUp(self):
        self.field = RatingRelatedField()
        self.internal_value = fixtures.Rating()
        self.bad_internal_value = MagicMock(spec=fixtures.Rating(), id=100)
        self.display_value = 'label'
        self.bad_display_value = 'bad-label'


class TestTagRelatedField(FieldTestCase):

    def setUp(self):
        self.field = TagRelatedField()
        self.internal_value = fixtures.Tag()
        self.bad_internal_value = MagicMock(spec=fixtures.Tag(), id=100)
        self.display_value = 'tag'
        self.bad_display_value = 'bad-tag'
