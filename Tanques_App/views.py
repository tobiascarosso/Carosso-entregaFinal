from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from Tanques_App.models import Tanque

# Create your views here.



def inicio(request):
    return render(request, 'apptanques/index.html')

def template1(request, nombre, apellido):
    return HttpResponse(f"hola compadre {nombre} {apellido}")

def template2(request, nombre, apellido):
    
    template = loader.get_template('template2.html')
    
    datos = {
            'nombre': nombre , 
            'apellido': apellido
             }
    
    template_renderizado = template.render(datos)
    
    return HttpResponse(template_renderizado)

def template3(request, nombre, apellido):
    
    datos = {
            'nombre': nombre , 
            'apellido': apellido
             }
    
    return render(request, 'template2.html', datos)

def agregar(request, unidad, pais, tripulantes):
    tanque = Tanque(unidad = unidad, pais = pais, tripulantes = tripulantes)
    tanque.save()
    return render(request, 'template_tanque/agregar.html', {"tanque": tanque})
