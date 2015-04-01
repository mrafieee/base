from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from models import *
from apps.views import paginate


def list(request, language):
    products_records = Product.objects.filter(language=language)
    products_records = paginate(request, products_records, 10)
    return render_to_response('product/list.html', {'products': products_records},
                              context_instance=RequestContext(request))


def detail(request, language, slug):
    product = get_object_or_404(Product, language=language, slug=slug)
    return render_to_response('product/detail.html', {'product': product}, context_instance=RequestContext(request))