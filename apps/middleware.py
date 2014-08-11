from django.http import HttpResponseRedirect
from django.conf import settings

IGNORE_SLUGS = ['admin', 'static', 'media', 'tiny_mce',]

class URLLanguageMiddleware():
    def process_request(self, request):
        slug = request.path.split('/')[1]

        if slug not in IGNORE_SLUGS:
            if slug in [code for code, name in settings.LANGUAGES]:
                request.language = set_language_code(request, slug)
            else:
                # Find and set the default language and redirect to it
                return HttpResponseRedirect('/%s%s' % (get_language_code(request), request.path))


def get_language_code(request):
    language = settings.LANGUAGE_CODE

    # TODO : What if the language is set in the session or the cookie but not equal to what we have in our settings?
    if 'django_language' in request.session:
        for code, name in settings.LANGUAGES:
            if code == request.session['django_language']:
                language = code
                break

    elif settings.LANGUAGE_COOKIE_NAME in request.COOKIES:
        for code, name in settings.LANGUAGES:
            if code == request.COOKIES[settings.LANGUAGE_COOKIE_NAME]:
                language = code
                break

    return language


def set_language_code(request, slug):
    language = get_language_code(request)
    if language != slug:
        for code, name in settings.LANGUAGES:
            if code == slug:
                language = code
                break
    request.session['django_language'] = language
    request.LANGUAGE_CODE = language
    request.COOKIES[settings.LANGUAGE_COOKIE_NAME] = language
    return language
