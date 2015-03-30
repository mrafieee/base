from django.conf.urls import patterns, include, url

urlpatterns = patterns('apps.contact.views',
    url(r'^(?P<language>[\w-]+)/contact-us/$', 'contact', name='contact-us'),
)