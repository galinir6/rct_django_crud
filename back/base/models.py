from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=5,decimal_places=2)
    category = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields =['desc','price','category']
 
    def __str__(self):
           return self.name