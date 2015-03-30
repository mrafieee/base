from django.conf.urls import patterns, include, url
from views import detail

urlpatterns = patterns('',
    url(r'^$', detail, name='flatpages-details'),
)