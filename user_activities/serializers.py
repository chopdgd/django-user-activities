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
    activities = serializers.SerializerMethodField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Comment
        fields = (
            'id', 'text', 'active',
            'activities', 'tags',
            'user', 'created', 'modified',
        )

    def get_activities(self, obj):

        content_type = ContentType.objects.get(model='comment')
        counts = models.Activity.objects.aggregate_counts(content_type, obj.id)

        result = {}
        for element in counts:
            key = str(choices.ACTIVITY_TYPES[element['activity_type']]).lower().replace(' ', '_')
            result[key] = element['total']

        # Add in user activities
        request = self.context.get("request")
        objs = models.Activity.objects.user_actions(request.user, content_type, obj.id)
        user_actions = [
            {
                'id': x['id'],
                'active': x['active'],
                'activity_type': choices.ACTIVITY_TYPES[x['activity_type']].lower(),
            }
            for x in objs
        ]

        result['user_actions'] = user_actions
        return result


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
    activities = serializers.SerializerMethodField()
    tags = serializers.StringRelatedField(many=True)
    rating = fields.RatingRelatedField(queryset=models.Rating.objects.all())

    class Meta:
        model = models.Comment
        fields = (
            'id', 'text', 'active',
            'rating', 'activities', 'tags',
            'user', 'created', 'modified',
        )

    def get_activities(self, obj):

        content_type = ContentType.objects.get(model='review')
        counts = models.Activity.objects.aggregate_counts(content_type, obj.id)

        result = {}
        for element in counts:
            key = str(choices.ACTIVITY_TYPES[element['activity_type']]).lower().replace(' ', '_')
            result[key] = element['total']

        # Add in user activities
        request = self.context.get("request")
        objs = models.Activity.objects.user_actions(request.user, content_type, obj.id)
        user_actions = [
            {
                'id': x['id'],
                'active': x['active'],
                'activity_type': choices.ACTIVITY_TYPES[x['activity_type']].lower(),
            }
            for x in objs
        ]

        result['user_actions'] = user_actions
        return result


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
