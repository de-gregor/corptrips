from django.urls import path,include
from django.contrib.auth import views
from . import views


app_name = 'settlement'

urlpatterns = [
   path('', views.home, name='home'),
   path('accounts/login/', views.login_view, name = 'login'),
   path('accounts/register/', views.register_view, name = 'register'),
 ]

