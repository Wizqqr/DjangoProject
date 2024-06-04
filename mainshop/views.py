from django.shortcuts import render
from . import models
from django.views import generic

class MainShopListGadget(generic.ListView):
    models = models.MainGadgets
    template_name = 'mainshop/mainshop_list.html'
    context_object_name = 'mainshops'

    def get_queryset(self):
        return models.MainGadgets.objects.all().order_by('-id')

# class MainShopListSales(generic.ListView):
#     models = models.Sales
#     template_name = 'mainshop/shopsale_list.html'
#     context_object_name = 'shopsales'
#
