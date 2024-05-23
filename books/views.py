from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from . import forms
from . import models

# def book_full_info(request, id):
#     if request.method == 'GET':
#         book = get_object_or_404(PostBooks, id=id)
#         reviews = book.reviews.all()
#         return render(request, 'book_full_info.html', {'book': book, 'reviews': reviews})

class BookList(generic.ListView):
    model = models.PostBooks
    template_name = 'books/book_list.html'
    context_object_name = 'books'

class BookFullInfo(generic.DetailView):
    template_name = 'books/book_full_info.html'
    context_object_name = 'book_id'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBooks, id=book_id)

class BookChange(generic.UpdateView):
    template_name = 'books/book_change.html'
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBooks, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookChange, self).form_valid(form=form)

class BookDelete(generic.DeleteView):
    template_name = 'books/book_delete.html'
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.PostBooks, id=book_id)

class BookAdd(generic.CreateView):
    template_name = 'books/book_add.html'
    success_url = '/books/'
    form_class = forms.BookForm

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(BookAdd, self).form_valid(form=form)

class SearchBookView(generic.ListView):
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    paginate_by = 5

    def get_queryset(self):
        return models.PostBooks.objects.filter(name__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['q'] = self.request.GET.get('q')
        return contex