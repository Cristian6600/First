from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField, DateField, IntegerField
from django.utils import timezone



# Create your models here.
class Nomina(models.Model):

    Fecha = models.DateField()
    Cta = models.IntegerField()
    D_C = models.CharField(max_length=2)
    Identificacion = models.CharField(max_length=15)
    Nombre = models.CharField(max_length=70)
    Codigo = models.CharField(max_length=8)
    Nombre_CC = models.CharField(max_length=20)
    Concepto =  models.CharField(max_length=40)
    Valor = models.IntegerField()

    class Meta:
        verbose_name = "Nomina"
        verbose_name_plural = "Nomina"
    

    def __str__(self):
       return self.Nombre

class Seguridad (models.Model):
    Fecha = models.DateField()
    Identificacion = models.CharField(max_length = 15 )
    Provision = models.CharField(max_length=20)
    Cta = models.IntegerField()
    D_C = models.CharField(max_length=1)
    Valor = models.DecimalField(max_digits=12, decimal_places=0)
    Nombre = models.CharField(max_length=60)
    Centro_Costo = models.CharField(max_length=20)
    Concepto = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Seguridad Social y Prestaciones"
        verbose_name_plural = "Seguridad Social y Prestaciones"

    def __str__(self):
       return self.Nombre








