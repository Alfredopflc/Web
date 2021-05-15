from django.urls import path
from home import views

app_name = "home"

urlpatterns = [
    path('list_leads/', views.ListLeadView.as_view(), name="list_leads"),
    path('detail_lead/<int:pk>/', views.DetailLeadView.as_view(), name = "detail_lead"),
    path('create_lead/', views.CreateLeadView.as_view(), name = "create_lead"),
    path('update_lead/<int:pk>/', views.UpdateLeadView.as_view(), name = "update_lead"),
    path('delete_lead/<int:pk>/', views.DeleteLeadView.as_view(), name = "delete_lead"),
]

