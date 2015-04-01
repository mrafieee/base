from django.utils.translation import ugettext_lazy as _
from django.db import models
from isecho import settings


class Product(models.Model):
    name = models.CharField(_('Name'), max_length=400)
    slug = models.SlugField(_('Slug'))
    image = models.ImageField(_('Product Image'), upload_to='uploads/products/', null=True, blank=True)
    description = models.TextField(_('Description'), null=True, blank=True)
    language = models.CharField(_('Language'), max_length=10, choices=settings.LANGUAGES, blank=False)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return "/products/%s/" % (self.slug)