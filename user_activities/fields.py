# -*- coding: utf-8 -*-
from django.core.exceptions import ObjectDoesNotExist
from django.utils.text import slugify

from rest_framework import serializers

from . import models


class RatingRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `rating` relationship.
    """

    def to_representation(self, value):
        try:
            return str(models.Rating.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('Rating Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        try:
            return models.Rating.objects.get(slug=slugify(value))
        except ObjectDoesNotExist:
            raise Exception('Rating: {0} not found!'.format(value))


class TagRelatedField(serializers.RelatedField):
    """
    A custom field to use for the `tag` relationship.
    """

    def to_representation(self, value):
        try:
            return str(models.Tag.objects.get(id=value.id))
        except ObjectDoesNotExist:
            raise Exception('Tag Id: {0} not found!'.format(value.id))

    def to_internal_value(self, value):
        try:
            return models.Tag.objects.get(slug=slugify(value))
        except ObjectDoesNotExist:
            raise Exception('Tag: {0} not found!'.format(value))
