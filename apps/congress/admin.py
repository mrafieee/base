from models import *
from django.contrib import admin


class MediaInline(admin.TabularInline):
    model = Media
    extra = 2
    exclude = ('type',)


class BoardDirectoryInline(admin.TabularInline):
	model = BoardDirectory
	extra = 5


class CongressAdmin(admin.ModelAdmin):
	inlines = [BoardDirectoryInline, MediaInline,]
	list_display = ('name','address','registration_phone','opening_date','closing_date','language',)
	list_per_page = 25
	list_filter = ['opening_date', 'closing_date', 'priority', 'language']
	search_fields = ('name',)
	ordering = ('opening_date',)
	prepopulated_fields = {'name': ['slug',]}
	save_on_top = True

class ArticleAdmin(admin.ModelAdmin):
	def accept_article(self,request,queryset):
		for item in queryset:
			item.status = 2
			item.save()
		return False
		
	def reject_article(self,request,queryset):
		for item in queryset:
			item.status = 1
			item.save()
		return False
		
	def pending_article(self,request,queryset):
		for item in queryset:
			item.status = 0
			item.save()
		return False
	accept_article.short_description = 'Accept Articles'
	reject_article.short_description = 'Reject Articles'
	pending_article.short_description = 'Pending Articles'
	list_display = ('last_name','first_name','email','phone','main_topic','status','code')
	list_per_page = 50
	search_fields = ('first_name','last_name','abstract','abstract_title','phone','code')
	list_filter = ['status','congress', 'main_topic',]
	actions = ['accept_article','reject_article','pending_article']


admin.site.register(Congress,CongressAdmin)
admin.site.register(Article,ArticleAdmin)
