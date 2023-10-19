from django.db import models
from django.urls import reverse


class School(models.Model):
    name = models.CharField(max_length=200)
    principal = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("schools:detail_school", kwargs={"pk": self.pk})
