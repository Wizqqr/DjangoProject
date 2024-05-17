from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

import datetime
from .models import PostBooks

def book_list(request):
    if request.method == 'GET':
        books = PostBooks.objects.all()
        return render(request, 'book_list.html', {'books': books})

def book_full_info(request, id):
    if request.method == 'GET':
        book = get_object_or_404(PostBooks, id=id)
        reviews = book.reviews.all()
        return render(request, 'book_full_info.html', {'book': book, 'reviews': reviews})

def my_bio(request):
    if request.method == 'GET':
        return HttpResponse('My name is Aziret, surname is Dzhumabekov and my age is 15')

def my_hobbies(request):
    if request.method == 'GET':
        return HttpResponse('My hobbies are studying maths, english, physics, chemistry and the favorite one IT. I go to the gym and swim but not every day')

def my_time(request):
    if request.method == 'GET':
        return HttpResponse('My time is: ')