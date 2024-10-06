from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Client, Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
