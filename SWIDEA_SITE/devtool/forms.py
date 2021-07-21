from django import forms
from django.forms import fields
from .models import Devtool

class DevForm(forms.ModelForm):
    class Meta:
        model = Devtool
        fields = '__all__'