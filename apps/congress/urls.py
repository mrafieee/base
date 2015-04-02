from django.conf.urls import patterns, url
from views import list, detail, up_coming, board_directory, time_table

urlpatterns = patterns('',
    url(r'^$', list),
    url(r'^up-coming/$', up_coming),
    url(r'^(?P<slug>[-\w]+)/board/$', board_directory),
    url(r'^(?P<slug>[-\w]+)/time-table/$', time_table),
    url(r'^(?P<slug>[-\w]+)/$', detail),
)