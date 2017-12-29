#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` urls module.
"""

from django.core.urlresolvers import reverse, resolve

from test_plus.test import TestCase

from .fixtures import Activity, Comment, Review


class TestUserActivitiesURLs(TestCase):
    """Test URL patterns for user activities."""

    def setUp(self):
        self.instance = Activity()

    def test_list_reverse(self):
        """user_activities:activity-list should reverse to /user-activities/."""
        self.assertEqual(reverse('user_activities:activity-list'), '/user-activities/')

    def test_list_resolve(self):
        """/user-activities/ should resolve to user_activities:activity-list."""
        self.assertEqual(resolve('/user-activities/').view_name, 'user_activities:activity-list')

    def test_detail_reverse(self):
        """user_activities:activity-detail should reverse to /user-activities/1/."""
        self.assertEqual(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            '/user-activities/1/'
        )

    def test_detail_resolve(self):
        """/user-activities/1/ should resolve to user_activities:activity-detail."""
        self.assertEqual(resolve('/user-activities/1/').view_name, 'user_activities:activity-detail')


class TestCommentsURLs(TestCase):
    """Test URL patterns for user comments."""

    def setUp(self):
        self.instance = Comment()

    def test_list_reverse(self):
        """user_activities:comment-list should reverse to /comments/."""
        self.assertEqual(reverse('user_activities:comment-list'), '/comments/')

    def test_list_resolve(self):
        """/comments/ should resolve to user_activities:comment-list."""
        self.assertEqual(resolve('/comments/').view_name, 'user_activities:comment-list')

    def test_detail_reverse(self):
        """user_activities:comment-detail should reverse to /comments/1/."""
        self.assertEqual(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            '/comments/1/'
        )

    def test_detail_resolve(self):
        """/comments/1/ should resolve to user_activities:comment-detail."""
        self.assertEqual(resolve('/comments/1/').view_name, 'user_activities:comment-detail')


class TestReviewsURLs(TestCase):
    """Test URL patterns for user reviews."""

    def setUp(self):
        self.instance = Review()

    def test_list_reverse(self):
        """user_activities:review-list should reverse to /reviews/."""
        self.assertEqual(reverse('user_activities:review-list'), '/reviews/')

    def test_list_resolve(self):
        """/reviews/ should resolve to user_activities:review-list."""
        self.assertEqual(resolve('/reviews/').view_name, 'user_activities:review-list')

    def test_detail_reverse(self):
        """user_activities:review-detail should reverse to /reviews/1/."""
        self.assertEqual(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            '/reviews/1/'
        )

    def test_detail_resolve(self):
        """/reviews/1/ should resolve to user_activities:review-detail."""
        self.assertEqual(resolve('/reviews/1/').view_name, 'user_activities:review-detail')
