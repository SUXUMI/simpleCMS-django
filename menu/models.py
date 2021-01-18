from django.db import models
from django.utils import timezone


class Menu(models.Model):
    sort = models.IntegerField()
    title = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    create_dt = models.DateTimeField(default=timezone.now)
    update_dt = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title