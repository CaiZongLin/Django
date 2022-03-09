from django.shortcuts import render

# Create your views here.

import json
import requests
from .models import Contact
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt

def contact(request):
	if 'name' in request.POST:
		name = request.POST['name']
		email = request.POST['email']
		subject = request.POST['subject']
		content = request.POST['content']

		obj = Contact.objects.create(
			name = name,
			email = email,
			subject = subject,
			content = content,
			)
		obj.save()
		
	return render(request, 'contact.html')




