from models import *
from django.contrib import admin


class AdAdmin(admin.ModelAdmin):
    list_filter = ('section', 'active', 'language')
    list_per_page = 25
    list_display = ( 'url', 'banner', 'section', 'priority', 'active', 'language')
    save_on_top = True


admin.site.register(Ad, AdAdmin)