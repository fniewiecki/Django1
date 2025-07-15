from django.http import HttpResponse
from django.urls import path
from . import views

urlpatterns = [
    path('ocen/', views.ocen_zdjecie, name='ocen'),
    path('dzieki/', lambda r: HttpResponse("Dzięki suko"), name='dzieki'),
]