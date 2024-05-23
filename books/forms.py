from django import forms
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.PostBooks
        fields = '__all__'