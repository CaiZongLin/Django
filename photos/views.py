from django.shortcuts import render, redirect

# Create your views here.

from .forms import UploadModelForm
from .models import Photo


def index(request):

    photos = Photo.objects.all() #抓取所有的照片資料

    form = UploadModelForm()  #生成物件，準備來做表單驗證

    if request.method == "POST":
        form = UploadModelForm(request.POST, request.FILES)
        if form.is_valid():  #表單驗證
            form.save()
            return redirect('/photos')

    context = {
        'photos': photos,
        'form': form
    }

    return render(request, 'photos.html', context)
