from django.db import models

# Create your models here.
class CharityOrg(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    telephone = models.CharField(max_length=20)
    mail = models.EmailField(max_length=250)
    location = models.CharField(max_length=200)