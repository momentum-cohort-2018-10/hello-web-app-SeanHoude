from django.db import models


class ClimbingShoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    # image = models.ImageField(max_length=50)
    # image = models.FilePathField(max_length=255, null=True, blank=True)

    # (IntegerField, CharField, BooleanField, FloatField, TextField)