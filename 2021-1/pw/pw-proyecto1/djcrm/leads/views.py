from django.shortcuts import render
from django.urls.base import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
#from django.contrib.auth.models import

from .models import Lead, Agent
from .forms import LeadForm, UpdateLeadForm, CustomUserCreationForm

from django.http import HttpResponse
from django.core import serializers

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from leads.serializers import LeadSerializer
from .models import Lead

@api_view(["GET", "POST"])
def list_lead(request):
    if request.method == "GET":
        queryset = Lead.objects.all()
        data = LeadSerializer(queryset, many = True)
        return Response(data.data, status = status.HTTP_200_OK)
    elif request.method =="POST":
        data = LeadSerializer(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data.data, status = status.HTTP_201_CREATED)
        return Response(data.errors, status = status.HTTP_400_BAD_REQUEST)




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







### AGENT ###
class ListAgentView(LoginRequiredMixin, generic.ListView):
    template_name = "leads/list_agent.html"
    #model = Lead
    #queryset = Lead.objects.all().order_by("register_timestamp")
    login_url = "leads:login"

    def get_queryset(self):
         return Agent.objects.all()


class DetailAgentView(LoginRequiredMixin, generic.DetailView):
    template_name= "leads/detail_agent.html"
    queryset= Agent.objects.all()
    login_url = "leads:login"

##SIGNUP USERS##
class Signup(generic.CreateView):
    template_name = "leads/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse('leads:index')


## ENDPOINT ##

#ws/vl/list_lead
def wsListLead(request):
    data = serializers.serialize("json", Lead.objects.all())
    return HttpResponse(data, content_type = "application/json")
    #return HttpResponse(data, content_type = "appLocation/json")

