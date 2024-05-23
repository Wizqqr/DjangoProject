from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse
from django.views import generic

class PhoneEditForm(generic.UpdateView):
    template_name = 'phones/edit.html'
    form_class = forms.PhoneForm
    success_url = '/phone_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Phone, id=phone_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneEditForm, self).form_valid(form=form)


class PhoneDeleteForm(generic.DeleteView):
    template_name = 'phones/confirm_delete.html'
    success_url = '/phone_list/'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Phone, id=phone_id)

class PhoneCreateComment(generic.CreateView):
    template_name = 'phones/phone_list.html'
    form_class = forms.CommentForm
    success_url = '/phone_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneCreateComment, self).form_valid(form=form)

class PhoneCreateForm(generic.CreateView):
    template_name = 'phones/create_phone.html'
    form_class = forms.PhoneForm
    success_url = '/phone_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(PhoneCreateForm, self).form_valid(form=form)

class PhoneDetailForm(generic.DetailView):
    template_name = 'phones/phone_detail.html'
    context_object_name = 'phone_id'

    def get_object(self, **kwargs):
        phone_id = self.kwargs.get('id')
        return get_object_or_404(models.Phone, id=phone_id)

class PhoneListView(generic.ListView):
    model = models.Phone
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    paginate_by = 5

    def get_queryset(self):
        return models.Phone.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = models.Comment.objects.all()
        context['comment_form'] = forms.CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        comment_form = forms.CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return redirect('phone_list')
        else:
            phones = self.get_queryset()
            comments = models.Comment.objects.all()
            context = self.get_context_data(object_list=phones)
            context['comments'] = comments
            context['comment_form'] = comment_form
            return render(request, self.template_name, context)

class SearchPhoneView(generic.ListView):
    template_name = 'phones/phone_list.html'
    context_object_name = 'phones'
    paginate_by = 5

    def get_queryset(self):
        return models.Phone.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex

