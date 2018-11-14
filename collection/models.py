from django.db import models

# Create your models here.
class ClimbingShoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)