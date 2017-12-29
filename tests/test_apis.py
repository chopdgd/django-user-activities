#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test django-user-activities
------------

Tests for `django-user-activities` API.
"""

from django.contrib.auth import get_user_model

try:
    from django.urls import reverse
except:
    from django.core.urlresolvers import reverse

from rest_framework import status
from rest_framework.test import APIClient, APITestCase

from . import fixtures


class TestUserActivityAPI(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = get_user_model().objects.create(username='username', email='email@email.com', password='password')
        self.client.force_authenticate(user=user)
        self.unauthorized_client = APIClient()

        # Create instance for GET, PUT, PATCH, DELETE Methods
        fixtures.Activity()

    def test_post(self):
        """Test POST."""

        data = {
            "activity_type": "favorite",
            "active": True,
            "content_type": "group",
            "object_id": 1,
            "user": "username"
        }

        response = self.client.post(
            reverse('user_activities:activity-list'),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_201_CREATED

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 2  # This is 2 because we already created another in setUp
        assert response_json['activity_type'] == 'favorite'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'group'
        assert response_json['object_id'] == 1
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'activity_type',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_get(self):
        """Test GET."""

        response = self.client.get(
            reverse('user_activities:activity-list'),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert len(response_json) == 1
        assert response_json[0]['id'] == 1
        assert response_json[0]['activity_type'] == 'favorite'
        assert response_json[0]['active'] is True
        assert response_json[0]['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json[0].keys())
        expected_keys = [
            'id',
            'activity_type',
            'active',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_put(self):
        """Test PUT."""

        data = {
            "activity_type": "like",
            "active": False,
            "content_type": "session",
            "object_id": 2,
            "user": "username"
        }

        response = self.client.put(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['activity_type'] == 'like'
        assert response_json['active'] is False
        assert response_json['content_type'] == 'session'
        assert response_json['object_id'] == 2
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'activity_type',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_patch(self):
        """Test PATCH."""

        data = {
            "activity_type": "like",
            "content_type": "session",
        }

        response = self.client.patch(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['activity_type'] == 'like'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'session'
        assert response_json['object_id'] == 1
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'activity_type',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_delete(self):
        """Test DELETE."""
        response = self.client.delete(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_permissions(self):
        """Make sure all endpoints are protected against unauthorized access."""

        get_response = self.unauthorized_client.get(
            reverse('user_activities:activity-list')
        )
        assert get_response.status_code == status.HTTP_403_FORBIDDEN

        detail_response = self.unauthorized_client.get(
            reverse('user_activities:activity-detail', kwargs={'pk': 1})
        )
        assert detail_response.status_code == status.HTTP_403_FORBIDDEN

        post_response = self.unauthorized_client.post(
            reverse('user_activities:activity-list'),
            {}
        )
        assert post_response.status_code == status.HTTP_403_FORBIDDEN

        put_response = self.unauthorized_client.put(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            {}
        )
        assert put_response.status_code == status.HTTP_403_FORBIDDEN

        patch_response = self.unauthorized_client.patch(
            reverse('user_activities:activity-detail', kwargs={'pk': 1}),
            {}
        )
        assert patch_response.status_code == status.HTTP_403_FORBIDDEN

        delete_response = self.unauthorized_client.delete(
            reverse('user_activities:activity-detail', kwargs={'pk': 1})
        )
        assert delete_response.status_code == status.HTTP_403_FORBIDDEN


class TestCommentAPI(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = get_user_model().objects.create(username='username', email='email@email.com', password='password')
        self.client.force_authenticate(user=user)
        self.unauthorized_client = APIClient()

        # Create instance for GET, PUT, PATCH, DELETE Methods
        fixtures.Comment()

    def test_post(self):
        """Test POST."""

        data = {
            "text": "text",
            "active": True,
            "content_type": "Comment",
            "object_id": 1,
            "user": "username"
        }

        response = self.client.post(
            reverse('user_activities:comment-list'),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_201_CREATED

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 2  # This is 2 because we already created another in setUp
        assert response_json['text'] == 'text'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'Comment'
        assert response_json['object_id'] == 1
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_get(self):
        """Test GET."""

        response = self.client.get(
            reverse('user_activities:comment-list'),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        # NOTE: This is what is created from fixture
        activities = {
            'favorite': 1,
            'user_actions': [
                {
                    'active': True,
                    'activity_type':
                    'favorite', 'id': 1
                }
            ]
        }

        response_json = response.json()
        assert len(response_json) == 1
        assert response_json[0]['id'] == 1
        assert response_json[0]['text'] == 'text'
        assert response_json[0]['active'] is True
        assert response_json[0]['activities'] == activities
        assert response_json[0]['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json[0].keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'activities',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_put(self):
        """Test PUT."""

        data = {
            "text": "text2",
            "active": False,
            "content_type": "Review",
            "object_id": 2,
            "user": "username"
        }

        response = self.client.put(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['text'] == 'text2'
        assert response_json['active'] is False
        assert response_json['content_type'] == 'Review'
        assert response_json['object_id'] == 2
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_patch(self):
        """Test PATCH."""

        data = {
            "content_type": "Review",
            "object_id": 2,
        }

        response = self.client.patch(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['text'] == 'text'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'Review'
        assert response_json['object_id'] == 2
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_delete(self):
        """Test DELETE."""
        response = self.client.delete(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_permissions(self):
        """Make sure all endpoints are protected against unauthorized access."""

        get_response = self.unauthorized_client.get(
            reverse('user_activities:comment-list')
        )
        assert get_response.status_code == status.HTTP_403_FORBIDDEN

        detail_response = self.unauthorized_client.get(
            reverse('user_activities:comment-detail', kwargs={'pk': 1})
        )
        assert detail_response.status_code == status.HTTP_403_FORBIDDEN

        post_response = self.unauthorized_client.post(
            reverse('user_activities:comment-list'),
            {}
        )
        assert post_response.status_code == status.HTTP_403_FORBIDDEN

        put_response = self.unauthorized_client.put(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            {}
        )
        assert put_response.status_code == status.HTTP_403_FORBIDDEN

        patch_response = self.unauthorized_client.patch(
            reverse('user_activities:comment-detail', kwargs={'pk': 1}),
            {}
        )
        assert patch_response.status_code == status.HTTP_403_FORBIDDEN

        delete_response = self.unauthorized_client.delete(
            reverse('user_activities:comment-detail', kwargs={'pk': 1})
        )
        assert delete_response.status_code == status.HTTP_403_FORBIDDEN


class TestReviewAPI(APITestCase):

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        user = get_user_model().objects.create(username='username', email='email@email.com', password='password')
        self.client.force_authenticate(user=user)
        self.unauthorized_client = APIClient()

        # Create instance for GET, PUT, PATCH, DELETE Methods
        fixtures.Review()

    def test_post(self):
        """Test POST."""

        data = {
            "text": "text",
            "rating": "label",
            "active": True,
            "content_type": "Comment",
            "object_id": 1,
            "user": "username"
        }

        response = self.client.post(
            reverse('user_activities:review-list'),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_201_CREATED

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 2  # This is 2 because we already created another in setUp
        assert response_json['text'] == 'text'
        assert response_json['rating'] == 'label'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'Comment'
        assert response_json['object_id'] == 1
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'rating',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_get(self):
        """Test GET."""

        response = self.client.get(
            reverse('user_activities:review-list'),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        # NOTE: This is what is created from fixture
        activities = {
            'favorite': 1,
            'user_actions': [
                {
                    'active': True,
                    'activity_type':
                    'favorite', 'id': 1
                }
            ]
        }

        response_json = response.json()
        assert len(response_json) == 1
        assert response_json[0]['id'] == 1
        assert response_json[0]['text'] == 'text'
        assert response_json[0]['active'] is True
        assert response_json[0]['rating'] == 'label'
        assert response_json[0]['activities'] == activities
        assert response_json[0]['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json[0].keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'rating',
            'activities',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_put(self):
        """Test PUT."""

        data = {
            "text": "text2",
            "rating": "label",
            "active": False,
            "content_type": "Review",
            "object_id": 2,
            "user": "username"
        }

        response = self.client.put(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['text'] == 'text2'
        assert response_json['rating'] == 'label'
        assert response_json['active'] is False
        assert response_json['content_type'] == 'Review'
        assert response_json['object_id'] == 2
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'rating',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_patch(self):
        """Test PATCH."""

        data = {
            "content_type": "Review",
            "object_id": 2,
        }

        response = self.client.patch(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            data,
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_200_OK

        # Make sure data is correct
        response_json = response.json()
        assert response_json['id'] == 1
        assert response_json['text'] == 'text'
        assert response_json['rating'] == 'label'
        assert response_json['active'] is True
        assert response_json['content_type'] == 'Review'
        assert response_json['object_id'] == 2
        assert response_json['user'] == 'username'

        # Make sure all expected keys are in the response
        observed_keys = list(response_json.keys())
        expected_keys = [
            'id',
            'text',
            'active',
            'content_type',
            'object_id',
            'user',
            'created',
            'modified'
        ]
        difference = set(expected_keys).difference(set(observed_keys))
        assert len(difference) == 0

    def test_delete(self):
        """Test DELETE."""
        response = self.client.delete(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            format='json'
        )

        # Make sure to recieve correct HTTP code
        assert response.status_code == status.HTTP_204_NO_CONTENT

    def test_permissions(self):
        """Make sure all endpoints are protected against unauthorized access."""

        get_response = self.unauthorized_client.get(
            reverse('user_activities:review-list')
        )
        assert get_response.status_code == status.HTTP_403_FORBIDDEN

        detail_response = self.unauthorized_client.get(
            reverse('user_activities:review-detail', kwargs={'pk': 1})
        )
        assert detail_response.status_code == status.HTTP_403_FORBIDDEN

        post_response = self.unauthorized_client.post(
            reverse('user_activities:review-list'),
            {}
        )
        assert post_response.status_code == status.HTTP_403_FORBIDDEN

        put_response = self.unauthorized_client.put(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            {}
        )
        assert put_response.status_code == status.HTTP_403_FORBIDDEN

        patch_response = self.unauthorized_client.patch(
            reverse('user_activities:review-detail', kwargs={'pk': 1}),
            {}
        )
        assert patch_response.status_code == status.HTTP_403_FORBIDDEN

        delete_response = self.unauthorized_client.delete(
            reverse('user_activities:review-detail', kwargs={'pk': 1})
        )
        assert delete_response.status_code == status.HTTP_403_FORBIDDEN
