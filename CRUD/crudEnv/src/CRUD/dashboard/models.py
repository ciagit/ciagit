from django.db import models

# Create your models here.
class Customer(models.Model):
    FirstName=models.CharField(max_length=20,null=True)
    lastName=models.CharField(max_length=20,null=True)
    address=models.CharField(max_length=50,null=True)
    
    def __str__(self):
        return self.FirstName