from django.shortcuts import render

# Create your views here.

from .models import Products
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import requests
import json

def product(request):
    
    pname = ""
    if 'qp' in request.GET: #去查詢request.GET是否有qp
        pname = request.GET['qp'] #取得html 內qp送出的東西
        pData = Products.objects.filter(name__contains=pname)
        
    else:
        pData = Products.objects.all().order_by('-id')
    
    
    
    
    paginator = Paginator(pData, 8) #一頁八個
    page = request.GET.get('page') #有就拿，沒有就不拿
    
    try:
        pData = paginator.page(page)
    except PageNotAnInteger:
        pData = paginator.page(1) #跳回第一頁
    except EmptyPage:
        pData = paginator.page(paginator.num_pages)
        
    
    
    
    
    
    #pData = Products.objects.all().order_by('-id')
    #pData = Products.objects.all().order_by('-id')[:10] #抓排序後的資料前10筆
    #pData = Products.objects.filter(price = 2084) #找到價格是2084 filter 是過濾的意思
    #pData = Products.objects.exclude(price='2084') #找出價格不是2084  exclude 是不等於的意思
    #pData = Products.objects.get(id='2')
    #pData = Products.objects.filter(price__gt = 1500) #找出價格大於1500  大於等於gte
    #pData = Products.objects.filter(price__lt = 1500)  #找出價格小於1500  小於等於lte
    #pData = Products.objects.filter(price__gte =s 1000,price__lte = 2000) 
    #pData = Products.objects.filter(price__range=[1000,2000]) #介於 (等同18行)
    #pData = Products.objects.filter(name__contains='休閒鞋') #contains 包含
    #pData = Products.objects.filter(name__startswith ='NIKE KD') #字首必須有
    #pData = Products.objects.filter(name__endswith ='4100') #字尾必須有
    
  
    content = {'product':pData,'pname':pname}
    
    return render(request,'product.html',content)



    








