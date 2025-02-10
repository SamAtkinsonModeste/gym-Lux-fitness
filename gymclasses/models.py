from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (("0", "Draft"), ("1", "Published"))


class GymClasses(models.Model):
    name = models.CharField(max_length=200, unique=True),
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, related_name="gymclasses")
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=STATUS, default="0")
    excert = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"Class: {self.name} created on {self.created_on} last updated on {self.updated_on}"
