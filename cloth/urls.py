from django.urls import path
from .views import cloth_list, for_boy, for_girl
urlpatterns = [
    path('shop/', cloth_list, name='shop'),
    path('shop/girls/', for_girl, name='girl'),
    path('shop/boys/', for_boy, name='boy'),
]