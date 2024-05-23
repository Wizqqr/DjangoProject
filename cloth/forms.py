from django import forms
from . import models

class ClothForm(forms.ModelForm):
    class Meta:
        model = models.Cloth
        fields = '__all__'