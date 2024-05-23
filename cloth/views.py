from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class ClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/cloth_list.html'
    context_object_name = 'clothes'

class GirlClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/girl.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Женское').order_by('-id')

class BoyClothListView(generic.ListView):
    model = models.Cloth
    template_name = 'clothes/boy.html'
    context_object_name = 'clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Мужское').order_by('-id')

class ClothDetailView(generic.DetailView):
    template_name = 'clothes/cloth_detail.html'
    context_object_name = 'cloth_id'

    def get_object(self, **kwargs):
        cloth_id = self.kwargs.get('id')
        return get_object_or_404(models.Cloth, id=cloth_id)

class ClothEditView(generic.UpdateView):
    template_name = 'clothes/cloth_edit.html'
    form_class = forms.ClothForm
    success_url = '/shop/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Cloth, id=phone_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ClothEditView, self).form_valid(form=form)

class ClothDeleteView(generic.DeleteView):
    template_name = 'clothes/confirm_delete.html'
    success_url = '/shop/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Cloth, id=phone_id)

class ClothCreateView(generic.CreateView):
    template_name = 'clothes/cloth_create.html'
    form_class = forms.ClothForm
    success_url = '/shop/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(ClothCreateView, self).form_valid(form=form)

