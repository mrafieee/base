from django.conf.urls import patterns, include, url
from views import list, detail

urlpatterns = patterns('',
    url(r'^$', list, name='event-list'),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='event-details'),
)