import os
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from datetime import datetime
from isecho.settings import LANGUAGES


class Event(models.Model):
    title = models.CharField(max_length=300, blank=False)
    slug = models.SlugField()
    image = models.ImageField(upload_to='uploads/events/', blank=True, null=True)
    body = models.TextField()
    from_date = models.DateField(blank=False, default=datetime.now())
    to_date = models.DateField(blank=True, null=True, default=None)
    language = models.CharField(max_length=6, blank=False, choices=LANGUAGES, default="en")


    def get_absolute_url(self):
        return '/'+ self.language+'/events/'+ self.slug +'/'


class Media(models.Model):
    def save(self, *args, **kwargs):
        self.type = self.get_type(self.file)

        # from middleware import threadlocals0
        # if threadlocals.get_current_user().is_authenticated():
        # self.user = threadlocals.get_current_user()
        super(Media, self).save(*args, **kwargs)

    def get_type(self, file):
        type = 'unknown'
        (dir, file) = os.path.split(str(file))

        (file_name, extension) = os.path.splitext(file)
        extension = extension.lower()
        for type in self.EXTENSIONS:
            if extension in type[1]:
                type = type[0]
                break
        return type

    def get_path(instance, filename):
        # TODO make upload directory like this return 'uploads/events/%s/%s', [instance.event.slug, filename]
        filename = "uploads/events/" + instance.event.slug + "/" + filename
        return filename

    EXTENSIONS = (
        ('image', ('.jpg', '.gif', '.png', '.bmp', '.jpeg')),
        ('video', ('.flv', '.wmv')),  # Done
        ('flash', ('.swf',)),  # Done
        ('sound', ('.mp3', '.wma')),  # Done
        ('doc', ('.doc', '.docx',)),  # Done
        ('powerpoint', ('.ppt', '.pptx', '.pps')),  # Done
        ('excel', ('.xls', '.xlsx')),  # Done
        ('text', ('.txt',)),  # Done
        ('pdf', ('.pdf',)),  # Done
        ('archive', ('.zip', '.rar', '.7z', '.gz', '.bz2')),  # Done
        'unknown'  # Done
    )
    file = models.FileField(_('File'), upload_to=get_path)
    thumb = models.FileField(_('File Thumbnail'), upload_to=get_path, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(_('Description'), max_length=256, blank=True, null=True)
    event = models.ForeignKey(Event, blank=True, null=True)


    class Meta:
        ordering = ('file',)

    def __unicode__(self):
        return str(self.file)
