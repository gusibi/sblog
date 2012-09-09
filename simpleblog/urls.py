#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.conf.urls import *


urlpatterns = patterns(('simpleblog.views'),
    (r'^bloglist/$', 'blog_list'),
    (r'^blog/(?P<id>\d+)/$', 'blog_show'),
    (r'^blog/(?P<id>\w+)/del/$', 'blog_del'),
    (r'^blog/(?P<id>\w+)/update/$', 'blog_update'),
    (r'^blog/add/$', 'blog_add'),
)
