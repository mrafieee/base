from django.db import models
from django.utils.translation import ugettext_lazy as _
from isecho.settings import LANGUAGES


class Ad(models.Model):
    class Meta:
        verbose_name = _('Ad')
        verbose_name_plural = _('Ads')
        ordering = ('priority', 'id',)

    SECTION_CHOICES = (
        # (0, _('Home Banner')),
        #(1, _('Farsi Home Banner')),
        (2, _('Sidebar Banner')),
    )
    PRIORITY_CHOICES = ((1, _('1 (Highest Priority)')), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9),
                        (10, _('10 (Lowest Priority)')))

    section = models.IntegerField(_('Section'), choices=SECTION_CHOICES, default=2)
    active = models.BooleanField(_('Active'), default=True)
    priority = models.IntegerField(_('Priority'), choices=PRIORITY_CHOICES, default=3)
    url = models.CharField(max_length=300, blank=True, null=True)
    banner = models.ImageField(_('Banner'), upload_to='uploads/ads/', null=True, blank=True,
                               help_text=_("200x100 px for sidebar Banners"))
    language = models.CharField(max_length=6, blank=False, choices=LANGUAGES, default="en")

    def __unicode__(self):
        return str(self.id)