from django.shortcuts import render
from django.http import HttpResponseRedirect #導轉
from django.contrib import messages #彈出視窗
from .models import Customer
import hashlib #加密
# Create your views here.
def customer(request):
    
    if 'username' in request.POST:
        
        username = request.POST['username']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['pwd']
        pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        #寫入資料庫
        Customer.objects.create(name = username,
                                sex = sex,
                                birthday = birthday,
                                email = email,
                                phone = phone,
                                address = address,
                                password = pwd,) #前面是變數，後面是資料表名稱

    if request.session.get('Ulogined',False) :  #若使用者已經登入，就轉到customer
        return render(request, 'customer.html')
    else:
        return HttpResponseRedirect('/login/')

def customer1(request):
    
    if 'username' in request.POST:
        
        username = request.POST['username']
        sex = request.POST['sex']
        birthday = request.POST['birthday']
        email = request.POST['email']
        address = request.POST['address']
        phone = request.POST['phone']
        password = request.POST['pwd']
        pwd = hashlib.sha256(password.encode('utf-8')).hexdigest()
        
        #寫入資料庫
        Customer.objects.create(name = username,
                                sex = sex,
                                birthday = birthday,
                                email = email,
                                phone = phone,
                                address = address,
                                password = pwd,) #前面是變數，後面是資料表名稱
        messages.error(request,'註冊成功')

        return HttpResponseRedirect('/login/')

    return render(request,'customer1.html')



def cusUpdate(request):

    if request.session.get('Ulogined',False) :
        if 'password' in request.POST:
            mail = request.session['userEmail']
            pwd = request.POST['password']

            obj = Customer.objects.get(email = mail)
            pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
            obj.password = pwd

            obj.save()

            messages.error(request,'修改成功')
            return HttpResponseRedirect('/')

        return render(request,'updateCus.html')
    else:
        return HttpResponseRedirect('/login/')


def login(request):
    if 'username' in request.POST:
        user = request.POST['username']  #使用者eamil
        pwd = request.POST['password']   #使用者密碼
        pwd = hashlib.sha256(pwd.encode('utf-8')).hexdigest()
        # 如果要用get時，資料庫中一定要有這個資料才可以
        #否則會出錯(不建議這樣作)
        #obj = Customer.objects.get(email=user,password=pwd)
        obj = Customer.objects.filter(email=user,password=pwd).count()

        if obj > 0 :
            request.session['Ulogined'] = True  #session 將使用者資料記憶在主機端，瀏覽器關閉就消失
            request.session['userEmail'] = user
            return HttpResponseRedirect('/')
        else:
            return render(request,'login.html')
    else:
        if request.session.get('Ulogined',False) :
            del request.session['Ulogined']
            if request.session.get('userEmail',"") != "":
                del request.session['userEmail']
        return render(request,'login.html')

def modifyInformation(request):

    if request.session.get('Ulogined',False) :
        if 'cusName' in request.POST:
            mail = request.session['userEmail']
            cusName = request.POST['cusName']
            cusPhone = request.POST['cusPhone']
            cusAddress = request.POST['cusAddress']

            obj = Customer.objects.get(email = mail)
            obj.name = cusName

            if request.POST['cusPhone'] == '':
                messages.error(request,'請輸入電話')
                return HttpResponseRedirect('/modifyInformation/')
            else:
                obj.phone = cusPhone
                
            if request.POST['cusAddress'] == '':
                messages.error(request,'請輸入地址')
                return HttpResponseRedirect('/modifyInformation/')
            else:
                obj.address = cusAddress
                
            """
            obj.phone = cusPhone
            obj.address = cusAddress
            """
            obj.save()
            
            messages.error(request,'修改成功')
            return HttpResponseRedirect('/')
    else:
        return HttpResponseRedirect('/login/')

    return render(request,'modifyInformation.html')