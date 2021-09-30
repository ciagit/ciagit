from django.db import models

# Create your models here.
class MyInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phoneNo = models.CharField(max_length=100)

class Experience(models.Model):
    workPosition = models.CharField(max_length=100)
    workDateFrom = models.DateField()
    workDateTo = models.DateField()
    workDescription = models.TextField(max_length=1000)

class Interest(models.Model):
    hobbies =models.CharField(max_length=200)
    hobbiesDes = models.TextField(max_length=200)

class Education(models.Model):
    uni_name = models.CharField(max_length=200)
    faculty =models.CharField(max_length=200)
    score = models.CharField(max_length=4)
    workDateFrom = models.DateField()
    workDateTo = models.DateField()
    

class Skills(models.Model):
    Languages = models.CharField(max_length=200)

class Awards(models.Model):
    achievements = models.CharField(max_length=200)

