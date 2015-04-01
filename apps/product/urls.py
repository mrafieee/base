from django.conf.urls import patterns, include, url
from views import list, detail

urlpatterns = patterns('',
    url(r'^$', list, name='product-list'),
    url(r'^(?P<slug>[\w-]+)/$', detail, name='product-details'),
)