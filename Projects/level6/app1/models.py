from django.db import models
from django.urls import reverse

# Create your models here.
class School(models.Model):
    name = models.CharField(max_length=200)
    principal = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app1:school_detail', kwargs={'pk': self.pk})
    

class Student(models.Model):
    school = models.ForeignKey(School,related_name='students', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('app1:school_detail' , kwargs={'pk': self.school.pk})
    

    
