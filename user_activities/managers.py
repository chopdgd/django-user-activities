# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Count, Q


class ActivityQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').all()

    def aggregate_counts(self, content_type, object_id, active=True):
        return self.fast().filter(
            Q(content_type=content_type) &
            Q(object_id=object_id) &
            Q(active=True)
        ).values('activity_type').annotate(total=Count('activity_type'))

    def user_actions(self, user, content_type, object_id):
        return self.fast().filter(
            Q(user__id=user.id) &
            Q(content_type=content_type) &
            Q(object_id=object_id)
        ).values('id', 'active', 'activity_type').distinct()


class CommentQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').prefetch_related('tags').all()


class ReviewQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').select_related('rating').prefetch_related('tags').all()
