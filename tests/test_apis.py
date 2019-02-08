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

import pytest
from rest_framework import status
from rest_framework.test import APIClient

from .fixtures import User, Activity, Comment, Rating, Review


@pytest.mark.django_db
def setup_client(user=None):
    client = APIClient()

    if user:
        client.force_authenticate(user=user)

    return client


def test_api_permissions():
    client = setup_client()

    response = client.get(reverse('user_activities:activity-list'))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(reverse('user_activities:activity-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.post(reverse('user_activities:activity-list'), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.put(reverse('user_activities:activity-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.patch(reverse('user_activities:activity-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.delete(reverse('user_activities:activity-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(reverse('user_activities:comment-list'))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(reverse('user_activities:comment-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.post(reverse('user_activities:comment-list'), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.put(reverse('user_activities:comment-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.patch(reverse('user_activities:comment-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.delete(reverse('user_activities:comment-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(reverse('user_activities:review-list'))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.get(reverse('user_activities:review-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.post(reverse('user_activities:review-list'), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.put(reverse('user_activities:review-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.patch(reverse('user_activities:review-detail', kwargs={'pk': 1}), {})
    assert response.status_code == status.HTTP_403_FORBIDDEN

    response = client.delete(reverse('user_activities:review-detail', kwargs={'pk': 1}))
    assert response.status_code == status.HTTP_403_FORBIDDEN


@pytest.mark.django_db
def test_delete_activity(User, Activity):
    user = User()
    Activity(id=20, user=user)
    client = setup_client(user=user)

    response = client.delete(reverse('user_activities:activity-detail', kwargs={'pk': 20}), format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_activity_list(User, Activity):
    user = User()
    Activity(user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:activity-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    observed_keys = list(response.json()[0].keys())
    expected_keys = [
        'id',
        'activity_type',
        'active',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_activity_detail(User, Activity):
    user = User()
    Activity(id=99, user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:activity-detail', kwargs={'pk': 99}), format='json')
    assert response.status_code == status.HTTP_200_OK

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'activity_type',
        'active',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_post_activity(User):
    user = User()
    client = setup_client(user=user)

    data = {
        "activity_type": "favorite",
        "active": True,
        "content_type": "group",
        "object_id": 1,
        "user": "username"
    }
    response = client.post(
        reverse('user_activities:activity-list'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'content_type',
        'object_id',
        'activity_type',
        'active',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_put_activity(User, Activity):
    user = User()
    Activity(id=99, user=user)
    client = setup_client(user=user)

    data = {
        "activity_type": "like",
        "active": False,
        "content_type": "session",
        "object_id": 305,
        "user": "username"
    }

    response = client.put(
        reverse('user_activities:activity-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
    observed_keys = list(response_json.keys())
    expected_keys = [
        'id',
        'content_type',
        'object_id',
        'activity_type',
        'active',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['activity_type'] == 'like'
    assert response_json['active'] is False
    assert response_json['content_type'] == 'session'
    assert response_json['object_id'] == 305
    assert response_json['user'] == 'username'


@pytest.mark.django_db
def test_patch_activity(User, Activity):
    user = User()
    Activity(id=99, user=user)
    client = setup_client(user=user)

    data = {
        "activity_type": "down_vote",
        "content_type": "session",
        "object_id": 954,
    }

    response = client.patch(
        reverse('user_activities:activity-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
    observed_keys = list(response_json.keys())
    expected_keys = [
        'id',
        'content_type',
        'object_id',
        'activity_type',
        'active',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['activity_type'] == 'down_vote'
    assert response_json['active'] is True
    assert response_json['content_type'] == 'session'
    assert response_json['object_id'] == 954
    assert response_json['user'] == 'username'


@pytest.mark.django_db
def test_delete_comment(User, Comment):
    user = User()
    Comment(id=20, user=user)
    client = setup_client(user=user)

    response = client.delete(reverse('user_activities:comment-detail', kwargs={'pk': 20}), format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_comment_list(User, Comment):
    user = User()
    Comment(user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:comment-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    observed_keys = list(response.json()[0].keys())
    expected_keys = [
        'id',
        'text',
        'active',
        'tags',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_comment_detail(User, Comment):
    user = User()
    Comment(id=99, user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:comment-detail', kwargs={'pk': 99}), format='json')
    assert response.status_code == status.HTTP_200_OK

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'text',
        'active',
        'tags',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_post_comment(User):
    user = User()
    client = setup_client(user=user)

    data = {
        "text": "text",
        "active": True,
        "content_type": "Comment",
        "object_id": 1,
        "user": "username"
    }
    response = client.post(
        reverse('user_activities:comment-list'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED

    observed_keys = list(response.json().keys())
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_put_comment(User, Comment):
    user = User()
    Comment(id=99, text='hi', user=user)
    client = setup_client(user=user)

    data = {
        "text": "text2",
        "active": False,
        "content_type": "Review",
        "object_id": 2,
        "user": "username"
    }

    response = client.put(
        reverse('user_activities:comment-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['text'] == 'text2'
    assert response_json['active'] is False
    assert response_json['content_type'] == 'Review'
    assert response_json['object_id'] == 2
    assert response_json['user'] == 'username'


@pytest.mark.django_db
def test_patch_comment(User, Comment):
    user = User()
    Comment(id=99, text='mike', user=user)
    client = setup_client(user=user)

    data = {
        "content_type": "Review",
        "active": False,
        "object_id": 2,
    }

    response = client.patch(
        reverse('user_activities:comment-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['text'] == 'mike'
    assert response_json['active'] is False
    assert response_json['content_type'] == 'Review'
    assert response_json['object_id'] == 2
    assert response_json['user'] == 'username'


@pytest.mark.django_db
def test_delete_review(User, Review):
    user = User()
    Review(id=20, user=user)
    client = setup_client(user=user)

    response = client.delete(reverse('user_activities:review-detail', kwargs={'pk': 20}), format='json')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_get_reivew_list(User, Review):
    user = User()
    Review(user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:review-list'), format='json')
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 1

    observed_keys = list(response.json()[0].keys())
    expected_keys = [
        'id',
        'text',
        'rating',
        'tags',
        'active',
        'content_type',
        'object_id',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_get_review_detail(User, Review):
    user = User()
    Review(id=99, user=user)
    client = setup_client(user=user)
    response = client.get(reverse('user_activities:review-detail', kwargs={'pk': 99}), format='json')
    assert response.status_code == status.HTTP_200_OK

    observed_keys = list(response.json().keys())
    expected_keys = [
        'id',
        'text',
        'rating',
        'tags',
        'active',
        'content_type',
        'object_id',
        'user',
        'created',
        'modified'
    ]
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_post_review(User, Rating):
    user = User()
    Rating(label='very good!')
    client = setup_client(user=user)

    data = {
        "text": "text",
        "rating": "very good!",
        "active": True,
        "content_type": "Comment",
        "object_id": 1,
        "user": "username"
    }
    response = client.post(
        reverse('user_activities:review-list'),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_201_CREATED

    observed_keys = list(response.json().keys())
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0


@pytest.mark.django_db
def test_put_review(User, Review, Rating):
    user = User()
    rating = Rating(label='very good!')
    Rating(label='very bad!')
    Review(id=99, text='hi', user=user, rating=rating)
    client = setup_client(user=user)

    data = {
        "text": "text2",
        "rating": "very bad!",
        "active": False,
        "content_type": "Comment",
        "object_id": 305,
        "user": "username"
    }

    response = client.put(
        reverse('user_activities:review-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['text'] == 'text2'
    assert response_json['rating'] == 'very bad!'
    assert response_json['active'] is False
    assert response_json['content_type'] == 'Comment'
    assert response_json['object_id'] == 305
    assert response_json['user'] == 'username'


@pytest.mark.django_db
def test_patch_review(User, Rating, Review):
    user = User()
    rating = Rating(label='very good!')
    Rating(label='very bad!')
    Review(id=99, text='mike', user=user, rating=rating)
    client = setup_client(user=user)

    data = {
        "rating": "very bad!",
        "content_type": "Comment",
        "active": False,
        "object_id": 954,
    }

    response = client.patch(
        reverse('user_activities:review-detail', kwargs={'pk': 99}),
        data,
        format='json'
    )
    assert response.status_code == status.HTTP_200_OK

    response_json = response.json()
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
    difference = set(observed_keys).difference(set(expected_keys))
    assert len(difference) == 0

    assert response_json['id'] == 99
    assert response_json['text'] == 'mike'
    assert response_json['rating'] == 'very bad!'
    assert response_json['active'] is False
    assert response_json['content_type'] == 'Comment'
    assert response_json['object_id'] == 954
    assert response_json['user'] == 'username'
