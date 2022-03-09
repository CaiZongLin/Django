from django.db import models

# Create your models here.

class OrdersModel(models.Model):
	subtotal = models.IntegerField(default=0)
	shipping = models.IntegerField(default=0) #運費
	grandtotal = models.IntegerField(default=0) 
	customname = models.CharField(max_length=100)
	customemail = models.CharField(max_length=200)
	customphone = models.CharField(max_length=20)
	customaddress = models.CharField(max_length=200)
	paytype = models.CharField(max_length=30)
	create_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customname

class DetailModel(models.Model):
	dorder = models.ForeignKey('OrdersModel',on_delete=models.CASCADE) #關聯鍵 對應的資料被刪掉，此資料一併刪除
	pname = models.CharField(max_length=100)
	unitprice = models.IntegerField(default=0)
	quantity = models.IntegerField(default=0)
	dtotal = models.IntegerField(default=0)

	def __str__(self):
		return self.pname


