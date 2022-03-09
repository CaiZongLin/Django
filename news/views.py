from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from datetime import datetime

from .models import News

import requests
import json

def index(request):
    return render(request,'index.html')


def news(request):
    
    allNews = News.objects.all().order_by('-id')
    content = {'news':allNews}
    return render(request,'news.html',content)
    
    
    # url = 'http://tbike-data.tainan.gov.tw/Service/StationStatus/Json'
    
    # data = requests.get(url).text
    # bike = json.loads(data)
    
    # station = list()
    
    # for item in bike:
    #     station.append(item['StationName'])
    
    
    
    
    # score = [100,89,60,70]
    
    # content = {'score':score,'display_time':str(datetime.now()),'ubike':station}
    
    # #{'display_time':str(datetime.now())}
    # return render(request,'news.html',content)