# example/simple/urls.py

from django.conf.urls import patterns, url

import views

urlpatterns = patterns('',
    url(r'^$', views.home),
    url(r'^([0-9]*)$', views.frame_by_index),
    url(r'^(0x[0-9a-fA-F]*)$', views.frame_by_eip)
)
