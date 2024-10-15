from django import forms
from airlines.models import Crew, Plane


class PlaneForm(forms.ModelForm):
    class Meta:
        model = Plane
        fields = ['plane_model', 'plane_type', 'range_of_flight', 'crew']
        widgets = {
            'crew': forms.CheckboxSelectMultiple(),
        }


class PlaneCreateForm(PlaneForm):
    pilots = forms.ModelMultipleChoiceField(
        queryset=Crew.objects.all(), widget=forms.CheckboxSelectMultiple
    )

    class Meta:
        model = Plane
        fields = ['plane_model', 'plane_type', 'range_of_flight', 'crew']
