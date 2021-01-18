from django.db import models
from django.utils import timezone


class Page(models.Model):
    title = models.CharField(max_length=255, blank=False)
    # slug = models.CharField(max_length=255, unique=True, blank=False)
    # https://www.geeksforgeeks.org/slugfield-django-models/
    slug = models.SlugField(max_length=64, unique=True)
    meta_description = models.CharField(max_length=255)
    content = models.TextField(null=True, blank=True)
    create_dt = models.DateTimeField(default=timezone.now)
    update_dt = models.DateTimeField(auto_now=True)

    # https://docs.djangoproject.com/en/2.2/ref/contrib/admin/actions/
    def __str__(self):
        return self.title
