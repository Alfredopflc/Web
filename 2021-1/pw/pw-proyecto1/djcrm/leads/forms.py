from django import forms

from .models import Lead

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