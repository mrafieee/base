from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render_to_response
from django.core.mail import send_mail
from apps.flatpages.models import Flatpage
from forms import ContactForm
from django.template import RequestContext
from isecho.settings import EMAIL_HOST_USER


def contact(request, language):
    try:
        flatpage = Flatpage.objects.get(slug='contact-us', language=language)
    except ObjectDoesNotExist:
        flatpage = None

    # print '*******************%s**************'%flatpage
    if 'POST' in request.method:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail('isecho.org', message, '%s<%s>' % (name, email), [EMAIL_HOST_USER], fail_silently=False)

            return render_to_response('contact/contact.html', {'flatpage': flatpage, 'success': 'success'},
                                      context_instance=RequestContext(request))

    else:
        form = ContactForm()

    return render_to_response('contact/contact.html', {'flatpage': flatpage, 'form': form, },
                              context_instance=RequestContext(request))