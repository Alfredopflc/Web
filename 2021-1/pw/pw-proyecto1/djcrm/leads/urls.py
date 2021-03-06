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
    path('login/', auth_views.LoginView.as_view(), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(), name = "logout"),

    ##path('login/', auth_views.LoginView.as_view(template_name = "leads/index.html"), name = "login"),
    ##path('logout/', auth_views.LogoutView.as_view(template_name = "leads/index.html"), name = "logout"),
    

    ## AGENT ##
    path('list_agent/', views.ListAgentView.as_view(),name="list_agent"),
    path('detail_agent/<int:pk>/', views.DetailAgentView.as_view(),name="detail_agent"),
    path('signup/', views.Signup.as_view(), name = "signup"),


    ##urls endpoint ws/vl
    path('ws/vl/list_lead', views.wsListLead, name = "wslistlead"),
    path('v1/list_leads/', views.list_lead, name = "list_lead"),
    path('v1/detail_update_delete_lead/<int:pk>/', views.detail_update_lead, name ="detail_update_delete"),
    path('ws/cliente/leads/', views.wsCliente, name = "wscliente"),

    path('ws/cliente/leads/post', views.wsClientPost, name ="wsclient_post")
]