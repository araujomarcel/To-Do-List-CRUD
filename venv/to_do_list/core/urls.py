from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('deletar/', views.deletar, name='deletar'),
    path('atualizar/', views.atualizar, name='atualizar'),
 
]