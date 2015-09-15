# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('myproject.myapp.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^search/$', 'search', name='search'),
    url(r'^view/$', 'view', name='view')
)
