from django.urls import path
from . import views

urlpatterns = [
    path('mainshop/', views.MainShopListGadget.as_view(), name='mainshop')
]