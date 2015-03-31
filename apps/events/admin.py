from models import *
from django.contrib import admin


class MediaAdmin(admin.ModelAdmin):
    list_display = ('type', 'description',)
    list_filter = ['type']
    search_fields = ('description', 'type',)
    list_per_page = 10
    save_on_top = True


class MediaInline(admin.TabularInline):
    model = Media
    extra = 2
    exclude = ('type',)


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'from_date', 'to_date', 'slug', 'language')
    list_per_page = 20
    list_filter = ['from_date', 'language']
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ['title', ]}
    save_on_top = True
    inlines = [MediaInline]


#admin.site.register(Media, MediaAdmin)
admin.site.register(Event, EventAdmin)
