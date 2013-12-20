#!
# urls.py from grids
from django.conf.urls import patterns, url

from grids import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^find/$', views.find_grid, name='find_form'),
    # url(r'^find/(?P<stem>\w+)$', views.find_stem, name='find_stem'),
    # url(r'^find/(?P<group>\w*)/(?P<machine>\w*)/(?P<phase>\w*)$', views.find, name='find'),
)