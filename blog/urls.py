from django.urls import path
from . import views

urlpatterns = [
    path('animales/', views.animales_list, name='animales_list'),
    path('protectoras/', views.protectoras_list, name='protectoras_list'),
    path('colaboradores/', views.colaboradores_list, name='colaboradores_list'),
]