# -*- coding: utf-8
from django.contrib import admin

from . import models


class ActivityAdmin(admin.ModelAdmin):
    model = models.Activity
    list_display = ('user', 'activity_type', 'content_type', 'object_id', 'active', 'created', 'modified')
    raw_id_fields = ('user', )
    search_fields = ('user__username', )
    list_filter = ('active', 'activity_type')
    save_as = True


class RatingAdmin(admin.ModelAdmin):
    model = models.Rating
    list_display = ('label', 'slug', 'active', 'created', 'modified')
    prepopulated_fields = {'slug': ('label', )}
    search_fields = ('label', )
    list_filter = ('active', )
    save_as = True


class TagAdmin(admin.ModelAdmin):
    model = models.Tag
    list_display = ('label', 'slug', 'active', 'created', 'modified')
    prepopulated_fields = {'slug': ('label', )}
    search_fields = ('label', )
    list_filter = ('active', )
    save_as = True


class CommentAdmin(admin.ModelAdmin):
    model = models.Comment
    list_display = ('user', 'content_type', 'object_id', 'active', 'created', 'modified')
    raw_id_fields = ('user', )
    search_fields = ('user__username', 'text')
    list_filter = ('active', )
    save_as = True


class ReviewAdmin(admin.ModelAdmin):
    model = models.Review
    list_display = ('user', 'content_type', 'object_id', 'rating', 'active', 'created', 'modified')
    raw_id_fields = ('user', )
    search_fields = ('user__username', 'text')
    list_filter = ('active', 'rating')
    save_as = True


admin.site.register(models.Activity, ActivityAdmin)
admin.site.register(models.Rating, RatingAdmin)
admin.site.register(models.Tag, TagAdmin)
admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Review, ReviewAdmin)
