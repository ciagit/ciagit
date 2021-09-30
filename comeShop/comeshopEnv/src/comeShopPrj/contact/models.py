from django.db import models

# Create your models here.
class Messages(models.Model):
    name = models.CharField(max_length=200,unique=True,blank=True,primary_key=True)
    email = models.EmailField(max_length=200)
    contact_no = models.CharField(max_length=10)
    message = models.TextField(max_length=100)
    