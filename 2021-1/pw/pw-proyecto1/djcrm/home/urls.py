from django.urls import path

from home import views

app_name = "home"

urlpatterns = [
    path('', views.Index.as_view(), name = "index" ),
    path('list/', views.list, name="list"),
    path('list_users/', views.ListUsers.as_view(), name="list_users"),
]