from django.urls import path
from Tanques_App import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('about', views.about),
    path('tanks/new/', views.agregar, name='creacion'),
    path('tanks/list/', views.listar, name='lista')
    
]
