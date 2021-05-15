from django import forms

from .models import Usuario

class LeadForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"


class UpdateLeadForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"