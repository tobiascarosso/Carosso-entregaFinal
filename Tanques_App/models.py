from django.db import models

# Create your models here.

class Tanque(models.Model):
    unidad = models.CharField(max_length=20) 
    pais = models.CharField(max_length=20)
    tripulantes = models.CharField(max_length=1)
    
    def __str__(self):
        return f'tanque {self.unidad}'
    