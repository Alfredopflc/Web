from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
#from django.contrib.auth.models import 

from .models import Usuario
from .forms import LeadForm, UpdateLeadForm
# Create your views here.

class Index(generic.TemplateView):
    template_name = "lead/index.html"

### C  R  U  D ###

### CREATE 
class CreateLeadView(generic.CreateView):
    template_name = "leads/create_lead.html"
    model = Usuario
    form_class = LeadForm
    success_url = reverse_lazy("home:list_leads")


### RETRIEVE
class ListLeadView(generic.ListView):
    template_name = "leads/list_leads.html"
    model = Usuario

class DetailLeadView(generic.DetailView):
    template_name= "leads/detail_lead.html"
    model = Usuario


### UPDATE

class UpdateLeadView(generic.UpdateView):
    template_name = "leads/update_lead.html"
    model = Usuario
    form_class = UpdateLeadForm
    success_url = reverse_lazy("home:list_leads")

### DELETE
class DeleteLeadView(generic.DeleteView):
    template_name = "leads/delete_lead.html"
    model = Usuario
    success_url = reverse_lazy("home:list_leads")
