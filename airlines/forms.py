from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from airlines.models import Crew, Plane, Order


class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = ['plane_model', 'plane_type', 'range_of_flight', 'crew']
        widgets = {
            'crew': forms.CheckboxSelectMultiple(),
        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'


class PlaneCreateForm(PlaneForm):
    pilots = forms.ModelMultipleChoiceField(
        queryset=Crew.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Plane
        fields = ['plane_model', 'plane_type', 'range_of_flight', 'crew']

