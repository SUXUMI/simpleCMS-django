from django.contrib import admin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    exclude = ('create_dt',)
    # fields = (('slug', 'title'), 'content')
    list_display = ('title', '_slug', 'update_dt')  # , 'create_dt'
    list_display_links = ('title',)

    ordering = ('create_dt',)

    def _slug(self, obj):
        uri = reverse('pages:view', args=[obj.slug])
        # return '/' + obj.slug
        return format_html('{} <a href="{}" target="_blank" title="View the link in new tab">↗</a>', uri, uri)

    _slug.short_description = 'URI'
    _slug.admin_order_field = 'slug'
    _slug.allow_tags = True

    def __str__(self):
        return 'sddd'

def __init__(self, *args, **kwargs):
    super(PageAdmin, self).__init__(*args, **kwargs)
    self.list_display_links = (None, )


# v1
# admin.site.register(Page)
