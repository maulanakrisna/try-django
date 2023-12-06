from django.db import models
from django.urls import reverse

# Create your models here.


class Article(models.Model):
    """docstring for Article."""
    title = models.CharField(max_length=120)  # max_length = required
    content = models.TextField(blank=True, null=True)
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("articles:article-detail", kwargs={"id": self.id})
