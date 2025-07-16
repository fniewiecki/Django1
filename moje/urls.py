from django.http import HttpResponse
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home, name='home'),
    path('ocen/', views.ocen_zdjecie, name='ocen'),
    path('dzieki/', lambda r: HttpResponse("Dzięki suko"), name='dzieki'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]