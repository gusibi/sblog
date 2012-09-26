#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.db import models


class Tag(models.Model):
    """docstring for Tags"""
    tag_name = models.CharField(max_length=20)
    create_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.tag_name


class Author(models.Model):
    """docstring for Author"""
    name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    website = models.URLField(blank=True)

    def __unicode__(self):
        return u'%s' % (self.name)


class BlogManager(models.Manager):
    """docstring for BlogManager"""
    def title_count(self, keyword):
        return self.filter(caption__icontains=keyword).count()

    def tag_count(self, keyword):
        return self.filter(tags__icontains=keyword).count()

    def author_count(self, keyword):
        return self.filter(author__icontains=keyword).count()


class Blog(models.Model):
    """docstring for Blogs"""
    caption = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    tags = models.ManyToManyField(Tag, blank=True)
    content = models.TextField()
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    count_objects = BlogManager()
    taglist = []

    def save(self, *args, **kwargs):
        super(Blog, self).save()
        for i in self.taglist:
            p, created = Tag.objects.get_or_create(tag_name=i)
            self.tags.add(p)

    def __unicode__(self):
        return u'%s %s %s' % (self.caption, self.author, self.publish_time)


class Weibo(models.Model):
    massage = models.CharField(max_length=200)
    author = models.ForeignKey(Author)
    publish_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.massage
