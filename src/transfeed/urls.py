from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'transfeed.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^delay/(\d{1,2})/$', 'transfeed.views.fn'),
    url(r'^admin/', include(admin.site.urls)),
)
