#!
# urls.py
from django.conf.urls import patterns, url

from runsets import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)