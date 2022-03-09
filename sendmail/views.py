from django.shortcuts import render

from email.mime.text import MIMEText
from smtplib import SMTP,SMTPAuthenticationError,SMTPException  #SMTP寄信用

# Create your views here.

def sendMail(request):
	smtp = "smtp.gmail.com:587"  #Gmail 主機位置
	account = "u103011305@cmu.edu.tw" #Gmail 帳號
	password = 's581115s'

	content = "非常感謝您的訂購,我們將快速出貨！"
	msg = MIMEText(content) #郵件內容

	msg["Subject"] = 'Lex購物城' #郵件主旨
	mailto = "u103011305@cmu.edu.tw"

	#mailto = ['u103011305@cmu.edu.tw','u10311304@cmu.edu.tw'] #多人

	server = SMTP(smtp) #建立連線
	server.ehlo() #跟主機溝通用
	server.starttls() #使用TTLS安全認證

	try:
		server.login(account,password) #登入
		server.sendmail(account,mailto,msg.as_string()) #寄信
		sendMsg = '郵件已寄出'
	except SMTPAuthenticationError:
		sendMsg = '無法登入！'
	except:
		sendMsg = '郵件發生錯誤'

	server.quit()

	return render(request,"sendMailPage.html",locals())
