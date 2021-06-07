from django.db import models
from django.db.models.fields import IntegerField

from applications.users.models import  User
# Create your models here.
#from users.models import User

# Create your models here.


class tipo_indicador(models.Model):
    Tipo = models.CharField(max_length=30, primary_key=True, unique=True)

    class Meta:
        verbose_name = "Tipo de indicador"
        verbose_name_plural = "Tipo de indicadores"

    def __str__(self):
      return self.Tipo

class indicador(models.Model):
    PE_CHOICES = [
        ('Enero',  'Enero'),
        ('Febrero',  'Febrero'),
        ('Marzo',  'Marzo'),
        ('Abril',  'Abril'),
        ('Mayo',  'Mayo'),
        ('Junio',  'Junio'),
        ('Julio',  'Julio'),
        ('Agosto',  'Agosto'),
        ('Septiembre',  'Septiembre'),
        ('Octubre',  'Octubre'),
        ('Nomviembre',  'Nomviembre'),
        ('Diciembre',  'Diciembre'),
      ]
    AÑO_CHOICES = [
        ('2021',  '2021'),
        ('2022',  '2022'),
        ('2023',  ''),
        ('2024',  ''),
        ('2025',  ''),
     
      ]     

    Tipo = models.ForeignKey(tipo_indicador, on_delete=models.CASCADE, verbose_name='indicador')
    Periodo = models.CharField(max_length=10, choices=PE_CHOICES)
    Año = models.CharField(max_length=4, choices=AÑO_CHOICES)
    meta = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Gestionad@s')
    limite = models.DecimalField(max_digits=6, decimal_places=2, verbose_name= 'Totales')
    aspectos = models.TextField(max_length=100,verbose_name = 'Aspectos a destacar del mes')
    solicitud = models.TextField(max_length=100,verbose_name = 'Solicitudes de recursos')  
    Porcentaje = models.DecimalField(max_digits=6, decimal_places=2, blank=True)


    @property
    def Porcentajes(self):
      return (self.meta / self.limite *100)

    def save(self):
        self.Porcentaje = self.Porcentajes
        super (indicador, self).save()
    
    def __str__(self):
        return self.solicitud

    class Meta:
        verbose_name = "Indicador"
        verbose_name_plural = "Indicadores"
        
    #dependencia = models.OneToOneField(
     #   dependencia,
     #   on_delete=models.CASCADE,
      #  total = property(_get_total)
      
    #def __unicode__(self):
     #   return self.solicitud + '' + self.dependencia

    #def __str__(self):    
    #    return "%s indicador" % self.dependencia

    #def __str__(self):
     #   return self.Año + ' ' + self.username



