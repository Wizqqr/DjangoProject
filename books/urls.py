from django.urls import path
from .views import my_bio, my_hobbies, my_time

urlpatterns = [
    path('bio/', my_bio),
    path('hobbies/', my_hobbies),
    path('time/', my_time),
]