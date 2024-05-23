from django.urls import path
from . import views

urlpatterns = [
    path('shop/', views.ClothListView.as_view(), name='shop'),
    path('shop/girls/', views.GirlClothListView.as_view(), name='girl'),
    path('shop/boys/', views.BoyClothListView.as_view(), name='boy'),
    path('shop/<int:id>/', views.ClothDetailView.as_view(), name='detail_view'),
    path('shop/<int:id>/update/', views.ClothEditView.as_view(), name='edit_view'),
    path('shop/<int:id>/delete/', views.ClothDeleteView.as_view(), name='delete_view'),
    path('shop/<int:id>/create', views.ClothCreateView.as_view(), name='create_view'),
    path('cloth_create/', views.ClothCreateView.as_view(), name='create_view'),
]