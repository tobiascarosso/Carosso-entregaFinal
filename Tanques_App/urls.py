from django.urls import path
from Tanques_App import views


urlpatterns = [
    path('', views.inicio),
    path('about', views.about),
    path('template1/<str:nombre>/<str:apellido>', views.template1),
    path('template2/<str:nombre>/<str:apellido>', views.template2),
    path('template3/<str:nombre>/<str:apellido>', views.template3),
    path('tanks/new/<str:unidad>/<str:pais>/<str:tripulantes>/', views.agregar)
]
