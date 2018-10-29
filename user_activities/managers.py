# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Count, Q


class ActivityQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').all()

    def aggregate_counts(self, content_type, object_id, active=True):
        counts_filter = Q(content_type=content_type)
        counts_filter &= Q(object_id=object_id)
        counts_filter &= Q(active=True)

        return self.fast()\
            .filter(counts_filter) \
            .values('activity_type') \
            .annotate(total=Count('activity_type'))

    def user_actions(self, user, content_type, object_id):
        actions_filter = Q(user__id=user.id)
        actions_filter &= Q(content_type=content_type)
        actions_filter &= Q(object_id=object_id)

        return self.fast() \
            .filter(actions_filter) \
            .values('id', 'active', 'activity_type') \
            .distinct()


class CommentQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').prefetch_related('tags').all()


class ReviewQuerySet(models.QuerySet):

    def fast(self):
        return self.select_related('user').select_related('rating').prefetch_related('tags').all()
