from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mares.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^mares/runsets/', include('runsets.urls', namespace='runsets')),
    url(r'^admin/', include(admin.site.urls)),
)
