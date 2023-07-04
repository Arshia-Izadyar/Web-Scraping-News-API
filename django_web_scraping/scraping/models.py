from django.db import models


class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=300, blank=True, null=True)
