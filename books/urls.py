from django.urls import path
from .views import my_bio, my_hobbies, my_time, book_list, book_full_info

urlpatterns = [
    path('bio/', my_bio, name='bio'),
    path('hobbies/', my_hobbies, name='hobbies'),
    path('time/', my_time, name='time'),
    path('books/', book_list, name = 'books'),
    path('books/<int:id>/', book_full_info, name='fullaboutbooks'),
]