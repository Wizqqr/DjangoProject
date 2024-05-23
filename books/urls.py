from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookList.as_view(), name = 'books'),
    path('books/<int:id>/', views.BookFullInfo.as_view(), name='fullaboutbooks'),
    path('books/<int:id>/update/', views.BookChange.as_view(), name='bookschange'),
    path('books/<int:id>/delete/', views.BookDelete.as_view(), name='booksdelete'),
    path('book_add/', views.BookAdd.as_view(), name='bookadd'),
    path('search/', views.SearchBookView.as_view(), name='search'),
]