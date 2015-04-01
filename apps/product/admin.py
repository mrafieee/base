from models import *
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name',)
    prepopulated_fields = {'slug': ['name', ]}


admin.site.register(Product, ProductAdmin)
