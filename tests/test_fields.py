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

from .fixtures import Rating, Tag


def RatingRelatedField():
    return fields.RatingRelatedField(read_only=True)


def TagRelatedField():
    return fields.TagRelatedField(read_only=True)


@pytest.mark.django_db
def test_to_representation_rating(Rating):
    field = RatingRelatedField()
    instance = Rating(label='look at me!')
    assert field.to_representation(instance) == 'look at me!'


@pytest.mark.django_db
def test_to_internal_value_rating(Rating):
    field = RatingRelatedField()
    instance = Rating(id=999, label='look at me!')
    assert field.to_internal_value('look at me!') == instance


@pytest.mark.django_db
def test_to_representation_failure_rating(Rating):
    field = RatingRelatedField()
    instance = MagicMock(spec=Rating(label='look at me!'), id=100)
    with pytest.raises(Exception):
        field.to_representation(instance)


@pytest.mark.django_db
def test_to_internal_value_failure_rating(Rating):
    field = RatingRelatedField()
    instance = MagicMock(spec=Rating(label='look at me!'), id=100)
    with pytest.raises(Exception):
        field.to_internal_value(instance)


@pytest.mark.django_db
def test_to_representation_tag(Tag):
    field = TagRelatedField()
    instance = Tag(label='this tag')
    assert field.to_representation(instance) == 'this tag'


@pytest.mark.django_db
def test_to_internal_value_tag(Tag):
    field = TagRelatedField()
    instance = Tag(id=999, label='this tag')
    assert field.to_internal_value('this tag') == instance


@pytest.mark.django_db
def test_to_representation_failure_tag(Tag):
    field = TagRelatedField()
    instance = MagicMock(spec=Tag(label='this tag'), id=100)
    with pytest.raises(Exception):
        field.to_representation(instance)


@pytest.mark.django_db
def test_to_internal_value_failure_tag(Tag):
    field = TagRelatedField()
    instance = MagicMock(spec=Tag(label='this tag'), id=100)
    with pytest.raises(Exception):
        field.to_internal_value(instance)
