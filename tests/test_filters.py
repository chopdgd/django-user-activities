#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` filters module.
"""

from django.test import TestCase

from user_activities import filters, models

from . import fixtures


class TestCommentFilter(TestCase):

    def setUp(self):
        fixtures.Comment()

    def test_filter_content_model(self):
        """Test content_model filter."""
        f = filters.CommentFilter(
            {'content_model': 'comment'},
            queryset=models.Comment.objects.all()
        )
        result = list(f.qs)

        assert len(result) == 1
        assert result[0].content_type.model == 'comment'


class TestReviewFilter(TestCase):

    def setUp(self):
        fixtures.Review()

    def test_filter_content_model(self):
        """Test content_model filter."""
        f = filters.ReviewFilter(
            {'content_model': 'review'},
            queryset=models.Review.objects.all()
        )
        result = list(f.qs)

        assert len(result) == 1
        assert result[0].content_type.model == 'review'
