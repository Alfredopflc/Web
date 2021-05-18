from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model

from .models import Lead

User = get_user_model()

class CustomUserCreationForm(UserCreationForm):
    class Meta:
            model = User
            fields = ("username",)
            fields_classes = {"username": UsernameField}


class LeadForm(forms.ModelForm):
    frist_name = forms.CharField(max_length = 32, widget=forms.TextInput(attrs={"placeholder": "Your Message", "class": "form-control"}))
    last_name = forms.CharField(max_length = 32, widget=forms.TextInput(attrs={"placeholder": "Your Message", "class": "form-control"}))
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ["register_timestamp", "regidter_update"]


class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = "__all__"
        exclude = ["register_timestamp", "regidter_update"]
#
