from django import forms
from . import models

class PhoneForm(forms.ModelForm):
    class Meta:
        model = models.Phone
        fields = '__all__'
class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = '__all__'


