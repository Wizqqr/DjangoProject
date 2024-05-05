from django.shortcuts import render
from django.http import HttpResponse
import datetime

def my_bio(request):
    if request.method == 'GET':
        return HttpResponse('My name is Aziret, surname is Dzhumabekov and my age is 15')

def my_hobbies(request):
    if request.method == 'GET':
        return HttpResponse('My hobbies are studying maths, english, physics, chemistry and the favorite one IT. I go to the gym and swim but not every day')

def my_time(request):
    if request.method == 'GET':
        current_time = datetime.datetime.now()
        return HttpResponse('My time is: ' + str(current_time))