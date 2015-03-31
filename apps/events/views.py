from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from apps.views import paginate
from models import *


def list(request, language):
    print(language)
    events = get_list_or_404(Event, language=language)
    events = paginate(request, events, 10)
    return render_to_response('events/list.html', {'events': events, 'language': language, 'request': request},
                              context_instance=RequestContext(request))


def detail(request, language, slug):
    print(language)
    print(slug)
    event = get_object_or_404(Event, slug=slug, language=language)
    event.medias = Media.objects.filter(event=event)
    return render_to_response('events/detail.html', {'event': event, 'language': language},
                              context_instance=RequestContext(request))
