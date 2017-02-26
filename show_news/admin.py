from django.contrib import admin
from .models import News, Sources

class SourceAdmin(admin.ModelAdmin):
	fields = ['name', 'url', 'code']
	list_display = ('name', 'check_source_online', 'print_code')

class NewsAdmin(admin.ModelAdmin):
	fields = ['source', 'headline', 'date', 'description']
	list_display = ('source', 'headline')
admin.site.register(Sources, SourceAdmin)
admin.site.register(News, NewsAdmin)
