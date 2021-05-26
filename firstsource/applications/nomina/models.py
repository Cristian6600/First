from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField, DateField, IntegerField

# Create your models here.
class Cargue (models.Model):
    Fecha = models.DateField()
    Identificacion = models.IntegerField(max_length=14)
    Descripcion = models.CharField(max_length=40)
    CODIGO_CC = models.CharField(max_length=10)
    Cuenta_Contable = models.IntegerField(max_length=10)
    Tipo = models.CharField(max_length=3)
    Valor = models.IntegerField(max_length=10)
    Nombre = models.CharField(max_length=80)
    Concepto = models.CharField(max_length=50)

#    def __str__(self):
 #       return self.Identificacion







