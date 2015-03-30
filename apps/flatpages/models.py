from django.db import models
from datetime import datetime
from isecho.settings import LANGUAGES


class Flatpage(models.Model):
    title = models.CharField(max_length=200, blank=False)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(blank=False, default=datetime.now())
    language = models.CharField(max_length=6, blank=False, choices=LANGUAGES, default="en")


