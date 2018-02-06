# -*- coding: utf-8 -*-
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType

from genomix.fields import ContentRelatedField, DisplayChoiceField, UserRelatedField
from rest_framework import serializers

from . import choices, fields, models


class ActivitySerializer(serializers.ModelSerializer):
    """Serializer for list and detail requests for User Activities."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    activity_type = DisplayChoiceField(choices=choices.ACTIVITY_TYPES)

    class Meta:
        model = models.Activity
        fields = (
            'id', 'activity_type', 'active',
            'user', 'created', 'modified',
        )


class ActivitySerializerCreateOrEdit(serializers.ModelSerializer):
    """Serializer for POST, PUT, PATCH requests for User Activities."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    activity_type = DisplayChoiceField(choices=choices.ACTIVITY_TYPES)
    content_type = ContentRelatedField(queryset=ContentType.objects.all())

    class Meta:
        model = models.Activity
        fields = (
            'id', 'activity_type', 'active',
            'content_type', 'object_id',
            'user', 'created', 'modified',
        )


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for list and detail requests for User Comments."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Comment
        fields = (
            'id', 'text', 'active', 'tags',
            'user', 'created', 'modified',
        )


class CommentSerializerCreateOrEdit(serializers.ModelSerializer):
    """Serializer for POST, PUT, PATCH requests for User Comments."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    content_type = ContentRelatedField(queryset=ContentType.objects.all())

    class Meta:
        model = models.Comment
        fields = (
            'id', 'text', 'active',
            'content_type', 'object_id',
            'user', 'created', 'modified',
        )


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for list and detail requests for User Reviews."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    tags = serializers.StringRelatedField(many=True)
    rating = fields.RatingRelatedField(queryset=models.Rating.objects.all())

    class Meta:
        model = models.Comment
        fields = (
            'id', 'text', 'active',
            'rating', 'tags',
            'user', 'created', 'modified',
        )


class ReviewSerializerCreateOrEdit(serializers.ModelSerializer):
    """Serializer for POST, PUT, PATCH requests for User Reviews."""

    user = UserRelatedField(queryset=get_user_model().objects.all())
    content_type = ContentRelatedField(queryset=ContentType.objects.all())
    rating = fields.RatingRelatedField(queryset=models.Rating.objects.all())

    class Meta:
        model = models.Review
        fields = (
            'id', 'text', 'rating', 'active',
            'content_type', 'object_id',
            'user', 'created', 'modified',
        )
