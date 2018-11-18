from django.db import models
from django.contrib.auth.models import User

class ClimbingShoe(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    slug = models.SlugField(unique=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
