from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=30,null=False)
    sex = models.CharField(max_length=2,default='F',null=False)
    birthday = models.DateField()
    email = models.EmailField(max_length=70,blank=True,default='')
    phone = models.CharField(max_length=10,blank=True,default='')
    address = models.CharField(max_length=200,blank=True,default='')
    password = models.CharField(max_length=100,null=False)
    create_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'customer'