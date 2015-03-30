from django.shortcuts import render_to_response, get_object_or_404  # , get_list_or_404
from django.template import RequestContext
from models import *


# def list(request, language):
# events = get_list_or_404(Event,language__code=language)
#     events = paginate(request,events, 10)
#     return render_to_response('events/list.html', {'events': events,'language':language})


def detail(request, language, slug):
    flatpage = get_object_or_404(Flatpage, slug=slug, language=language)
    return render_to_response('flatpages/detail.html', {'flatpage': flatpage, 'language': language},
                              context_instance=RequestContext(request))
