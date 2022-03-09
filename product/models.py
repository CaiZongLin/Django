from django.db import models

# Create your models here.


class Products(models.Model):
    brand = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    size = models.DecimalField(max_digits=4,decimal_places=1) #max_digits:最大的數 decimal_places：小数的最大位数
    color = models.CharField(max_length=30)
    price = models.IntegerField() #整數
    photo_url = models.CharField(max_length=200)
    discount = models.DecimalField(max_digits=4,decimal_places=2)
    
    class Meta:
        db_table = 'product'
























