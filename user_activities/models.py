# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.db import models
from django.utils.translation import ugettext_lazy as _

from genomix.models import TimeStampedLabelModel
from model_utils.models import TimeStampedModel

from . import choices, managers


class UserActivity(TimeStampedModel):
    """
    An abstract base class model that provides timestamps and auth information
    about who created, modified a user activity.
    """
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    text = models.CharField(max_length=255, blank=True)
    active = models.BooleanField(default=True)
    activities = GenericRelation('user_activities.Activity')
    tags = models.ManyToManyField('user_activities.Tag', blank=True)

    # Mandatory fields for generic relation
    # See: https://docs.djangoproject.com/en/1.11/ref/contrib/contenttypes/#generic-relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        abstract = True


class Activity(TimeStampedModel):
    """Track user likes, votes, etc."""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    activity_type = models.SmallIntegerField(choices=choices.ACTIVITY_TYPES)
    active = models.BooleanField(default=True)

    # Mandatory fields for generic relation
    # See: https://docs.djangoproject.com/en/1.11/ref/contrib/contenttypes/#generic-relations
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    objects = managers.ActivityQuerySet.as_manager()

    class Meta:
        verbose_name = _('Activity')
        verbose_name_plural = _('Activities')
        unique_together = ('user', 'activity_type', 'content_type', 'object_id',)

    def __str__(self):
        return self.get_activity_type_display()


class Rating(TimeStampedLabelModel):
    """Ratings"""

    class Meta:
        verbose_name = _('Rating')
        verbose_name_plural = _('Ratings')

    def __str__(self):
        return self.label


class Tag(TimeStampedLabelModel):
    """Tags"""

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tag')

    def __str__(self):
        return self.label


class Comment(UserActivity):
    """User comments."""

    comments = GenericRelation('user_activities.Comment')
    pinned = models.BooleanField(default=False)

    objects = managers.CommentQuerySet.as_manager()

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def __str__(self):
        return self.text


class Review(UserActivity):
    """User reviews."""

    rating = models.ForeignKey(
        'user_activities.Rating',
        related_name='reviews',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    comments = GenericRelation('user_activities.Comment')
    pinned = models.BooleanField(default=False)

    objects = managers.ReviewQuerySet.as_manager()

    class Meta:
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return self.text
