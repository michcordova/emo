from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='inicio'),
    path('inicio/', views.index, name='index'),
    path('about/', views.about, name='acercade'),
    path('mision/', views.mision, name='mision'),
    path('vision/', views.vision, name='vision'),
    path('registro/', views.registro, name='registro'),
    path('Inicio_sesion/', views.inicio_sesion, name='inicio_sesion'),
    path('logout/', views.logout, name='logout'),
]
