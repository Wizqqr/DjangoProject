from django.shortcuts import render
from .models import Cloth

def cloth_list(request):
    if request.method == 'GET':
        clothes = Cloth.objects.all()
        return render(request, 'clothes/cloth_list.html', {'clothes': clothes})

def for_girl(request):
    if request.method == 'GET':
        clothes = Cloth.objects.filter(tags__name='Женское').order_by('-id')
        return render(request, 'clothes/girl.html', {'clothes': clothes})

def for_boy(request):
    if request.method == 'GET':
        clothes = Cloth.objects.filter(tags__name='Мужское').order_by('-id')
        return render(request, 'clothes/boy.html', {'clothes': clothes})