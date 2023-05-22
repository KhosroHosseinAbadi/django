from django.db import models
    
class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    password1 = models.CharField(max_length=32)
    password2 = models.CharField(max_length=32)

    def __str__(self):
        return self.username