from django.utils.html import format_html
from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    exclude = ('create_dt',)
    list_display_links = ('title',)
    list_display = ('sort', 'title', '_url')
    ordering = ('sort',)

    list_editable = ('sort',)

    def _url(self, obj):
        return format_html('{} <a href="{}" target="_blank" title="View the link in new tab">↗</a>', obj.url, obj.url)
