from django.urls import path
from django.contrib.auth import views as auth_views

from leads import views

app_name = "leads"

urlpatterns = [
    path('', views.Index.as_view(), name="index"),
    path('list_leads/', views.ListLeadView.as_view(), name="list_leads"),
    path('detail_lead/<int:pk>/', views.DetailLeadView.as_view(), name = "detail_lead"),
    path('create_lead/', views.CreateLeadView.as_view(), name = "create_lead"),
    path('update_lead/<int:pk>/', views.UpdateLeadView.as_view(), name = "update_lead"),
    path('delete_lead/<int:pk>/', views.DeleteLeadView.as_view(), name = "delete_lead"),
    path('login/', auth_views.LoginView.as_view(template_name = "leads/index.html"), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name = "leads/index.html"), name = "logout"),

    ## AGENT ##
    path('list_agent/', views.ListAgentView.as_view(),name="list_agent"),
    path('detail_agent/<int:pk>/', views.DetailAgentView.as_view(),name="detail_agent"),

]