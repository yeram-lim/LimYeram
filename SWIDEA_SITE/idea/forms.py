from django import forms
from django.forms import fields
from .models import IdeaList

class IdeaForm(forms.ModelForm):
    class Meta:
        model = IdeaList
        fields = '__all__'