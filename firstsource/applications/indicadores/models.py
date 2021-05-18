from django.db import models

from applications.users.models import User, dependencia
# Create your models here.
#from users.models import User

# Create your models here.


class tipo_indicador(models.Model):
    Tipo = models.CharField(max_length=30)

    def __str__(self):
      return self.Tipo

class indicador(models.Model):
    PE_CHOICES = [
        ('EN',  'Enero'),
        ('FE',  'Febrero'),
        ('MAR',  'Marzo'),
        ('ABR',  'Abril'),
        ('MAY',  'Mayo'),
        ('JUN',  'Junio'),
        ('JUL',  'Julio'),
        ('AGO',  'Agosto'),
        ('SEP',  'Septiembre'),
        ('OCT',  'Octubre'),
        ('NOV',  'Nomviembre'),
        ('DIC',  'Diciembre'),
      ]
    AÑO_CHOICES = [
        ('2021',  '2021'),
        ('2022',  '2022'),
        ('2023',  ''),
        ('2024',  ''),
        ('2025',  ''),
     
      ]     

    Dependencia = models.OneToOneField(
        dependencia,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    Tipo = models.ForeignKey(tipo_indicador, on_delete=models.CASCADE)
    Periodo = models.CharField(max_length=6, choices=PE_CHOICES)
    Año = models.CharField(max_length=4, choices=AÑO_CHOICES)
    meta = models.IntegerField()
    limite = models.IntegerField(verbose_name= 'limite superior')
    aspectos = models.TextField(max_length=100,
    verbose_name = 'Aspectos a destacar del mes')
    solicitud = models.TextField(max_length=100,
    verbose_name = 'Solicitudes de recursos')
    
    #dependencia = models.OneToOneField(
     #   dependencia,
     #   on_delete=models.CASCADE,
      #  
    def __str__(self):
        return self.solicitud





      
      


      
    #def __unicode__(self):
     #   return self.solicitud + '' + self.dependencia

    #def __str__(self):    
    #    return "%s indicador" % self.dependencia

    #def __str__(self):
     #   return self.Año + ' ' + self.username



