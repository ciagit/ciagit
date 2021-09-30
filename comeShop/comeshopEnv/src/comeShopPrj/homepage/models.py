from django.db import models

# Create your models here.
class products(models.Model):
    item_name = models.CharField(max_length=200,null=True)
    item_price = models.CharField(max_length=100)
    item_des = models.TextField(max_length=400)
    item_pic = models.ImageField(upload_to='images/',null=True)
    def __str__(self):
        return self.item_name



        