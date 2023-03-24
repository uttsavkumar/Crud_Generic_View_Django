from django.db import models

# Create your models here.

class StudentRecord(models.Model):
    name = models.CharField( max_length=50)
    contact = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)

    