from django.db import models


class Sound(models.Model):
    title = models.CharField(max_length=32)
    slug = models.SlugField(max_length=32)
    soundcloud_id = models.CharField(max_length=48)
