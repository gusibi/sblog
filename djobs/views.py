#!/usr/bin/python
# -*- coding: utf-8 -*-

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from django.shortcuts import render_to_response
import time
import datetime


def hello(request):
    return HttpResponse("hello world")


def current_datetime(request):
    now = time.ctime()
    t = get_template('mytemp.html')
    html = t.render(Context({'current_date': now}))
    return HttpResponse(html)


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    links = ['link1','link2','link3','link4']
    current_date = datetime.datetime.now()
    hours_ahead = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('mytemp.html', locals())


def request_meta(request):
    values = request.META.items()
    values.sort()
    return render_to_response('request_meta.html', {'values': values})
