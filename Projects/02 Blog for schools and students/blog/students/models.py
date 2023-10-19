from django.db import models
from django.urls import reverse
from schools.models import School

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    school = models.ForeignKey(School, related_name="students", on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("schools:detail_school" , kwargs={"pk": self.school.pk})
