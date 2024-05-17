from django.shortcuts import render, get_object_or_404, redirect
from . import models, forms
from django.http import HttpResponse


def edit_phone_view(request, id):
    phone_id = get_object_or_404(models.Phone, id=id)
    if request.method == 'POST':
        form = forms.PhoneForm(request.POST, instance=phone_id)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Edit a phone</h1>')
    else:
        form = forms.PhoneForm(instance=phone_id)

    return render(request, template_name='phones/edit.html',
         context={
             'phone_id': phone_id,
             'form': form
         })

def delete_phone_view(request, id):
    phone_id = get_object_or_404(models.Phone, id=id)
    phone_id.delete()
    return HttpResponse('<h1>Delete a phone</h1>')
def create_phone_view(request):
    if request.method == 'POST':
        form = forms.PhoneForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Create a new phone</h1>')
    else:
        form = forms.PhoneForm()

    return render(request, template_name='phones/create_phone.html',
         context={'form': form})


def phone_detail(request, id):
    if request.method == 'GET':
        phone_id = get_object_or_404(models.Phone, id=id)
        return render(request, template_name='phones/phone_detail.html',
                      context={'phone_id': phone_id})


def phone_list(request):
    phones = models.Phone.objects.all()
    return render(request, 'phones/phone_list.html', {'phones': phones})

def add_comment(request, id):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('phone_list')  # Перенаправление на страницу с подтверждением
    else:
        form = forms.CommentForm()
    return render(request, 'add_comment.html', {'form': form})

def add_comment_success(request):
    return render(request, 'add_comment_success.html')