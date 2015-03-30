from models import *
from django.contrib import admin


class FlatpagesAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'language', 'slug',)
    list_per_page = 20
    list_filter = ['date', 'language']
    search_fields = ('title', 'body',)
    prepopulated_fields = {'slug': ['title', ]}
    save_on_top = True


admin.site.register(Flatpage, FlatpagesAdmin)
