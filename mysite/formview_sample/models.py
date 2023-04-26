from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()

    def get_absolute_url(self):
        return reverse("author-detail", kwargs={"pk": self.pk})
