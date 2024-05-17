from django.urls import path
from . import views

urlpatterns = [
    path('phone_list/', views.phone_list, name='phone_list'),
    path('phone_list/<int:id>/', views.phone_detail, name='phone_detail'),
    path('phone_list/<int:id>/delete/', views.delete_phone_view, name='phone_detail_delete'),
    path('phone_list/<int:id>/update/', views.edit_phone_view, name='phone_update_view'),
    path('create_phone/', views.create_phone_view, name='create_phone'),
    path('add_comment_phone/', views.add_comment_phone_view, name='add_comment_phone'),
]