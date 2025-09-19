from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_exposiciones, name='lista_exposiciones'),
]
