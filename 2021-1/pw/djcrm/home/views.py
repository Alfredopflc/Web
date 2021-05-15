from django.shortcuts import render
from django.views import generic
from django.contrib.auth.models import User
# Create your views here.


class Index(generic.TemplateView):
    template_name = "home/index.html"

    def get(self, request):
        numbers = [i for i in range(10)]
        context = {
            'message': "Hola Mundo, VENEGAS MEDINA",
            'numbers': numbers,
        }
        return render(request, "home/index.html", context)


def list(request):
    context = {
        "users": User.objects.all()
    }
    return render(request, "home/list.html", context)

class ListUsers(generic.ListView):
    model = User
    template_name= "home/list.html"

