from django import forms
from django.contrib.auth.forms import UserCreationForm
from airlines.models import Client


class DriverCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Client
        fields = UserCreationForm.Meta.fields + (
            "username",
            "last_name",
            "first_name",
            "license_number",
        )
