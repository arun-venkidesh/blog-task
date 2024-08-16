from django.db import models

# Create your models here.

class poems(models.Model):
    Title=models.CharField(max_length=50)
    Description=models.CharField(max_length=255)
    Date=models.CharField(max_length=255, null=True)
    Author=models.CharField(max_length=50)