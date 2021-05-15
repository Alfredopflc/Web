from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import

from .models import Lead, Agent
from .forms import LeadForm, UpdateLeadForm
# Create your views here.

class Index(generic.TemplateView):
    template_name = "leads/index.html"

    def get(self, request):
        queryset1 = Agent.objects.all()
        queryset2 = Lead.objects.all()

        context = {
            "obj1": queryset1,
            "obj2": queryset2
        }
        return render(request, "leads/index.html", context)

### C  R  U  D ###

### CREATE 
class CreateLeadView(LoginRequiredMixin, generic.CreateView):
    template_name = "leads/create_lead.html"
    model = Lead
    form_class = LeadForm
    success_url = reverse_lazy("leads:list_leads")
    login_url = "leads:login"


### RETRIEVE
class ListLeadView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/list_leads.html"
    #model = Lead
    #queryset = Lead.objects.all().order_by("register_timestamp")
    login_url = "leads:login"

    def get_queryset(self):
         return Lead.objects.all().order_by("-register_timestamp")
#
class DetailLeadView(LoginRequiredMixin, generic.DetailView):
    template_name= "leads/detail_lead.html"
    queryset= Lead.objects.all()
    login_url = "leads:login"

    def get_queryset(self):
        #print(self.get_queryset())
        return super().get_queryset()

### UPDATE
class UpdateLeadView(LoginRequiredMixin, generic.UpdateView):
    template_name = "leads/update_lead.html"
    model = Lead
    form_class = UpdateLeadForm
    success_url = reverse_lazy("leads:list_leads")
    login_url = "leads:login"

### DELETE
class DeleteLeadView(LoginRequiredMixin, generic.DeleteView):
    template_name = "leads/delete_lead.html"
    model = Lead
    success_url = reverse_lazy("leads:list_leads")
    login_url = "leads:login"