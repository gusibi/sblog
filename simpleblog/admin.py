#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.contrib import admin
from simpleblog.models import Author, Blog, Tag, Weibo


class AuthorAdmin(admin.ModelAdmin):
    """docstring for AuthorAdmin"""
    list_display = ('name', 'email', 'website')
    search_fields = ('name',)


class BlogAdmin(admin.ModelAdmin):
    """docstring for BlogAdmin"""
    list_display = ('caption', 'id', 'author', 'publish_time')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'
    ordering = ('-publish_time',)
    filter_horizontal = ('tags',)
    raw_id_fields = ('author',)  # 它是一个包含外键字段名称的元组，它包含的字段将被展现成`` 文本框`` ，而不再是`` 下拉框`` 。


admin.site.register(Author, AuthorAdmin)
admin.site.register(Blog, BlogAdmin)
admin.site.register(Tag)
admin.site.register(Weibo)
