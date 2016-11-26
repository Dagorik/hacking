from django import forms
from django.forms import ModelForm

class bastonForm(forms.Form):
    comentario = forms.CharField(max_length = 50)