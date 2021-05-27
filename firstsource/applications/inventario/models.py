from django.db import models
from django.db.models.fields import CharField
from applications.users.models import User, Areas


class Marcas(models.Model):
    marca = models.CharField(max_length=18)
    

    def __str__(self):
        return self.marca 

class Licencia(models.Model):
    serial = models.CharField(max_length=45)
    software = models.CharField(max_length=25)

    def __str__(self):
        return self.serial

class Hardware(models.Model):
    Hardware = models.CharField(max_length=30) 

    def __str__(self):
        return self.Hardware


class Inventario(models.Model):
    Serial = models.CharField(max_length=30)
    Producto = models.ForeignKey(Hardware, on_delete=models.CASCADE, verbose_name= 'Hardware')
    Marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=30)
    Estado = models.BooleanField(default=False)
    Ubicacion = models.ForeignKey(Areas, on_delete=models.CASCADE)
    Observacion = models.TextField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Licencia = models.ManyToManyField(Licencia)
    
    
    def __str__(self):
        return self.Serial


class Articulo(models.Model):
    Articulo = models.CharField(max_length=30)


class inmobiliario(models.Model):
    serial= models.CharField(max_length=20)
    Articulo= models.ForeignKey(Articulo, on_delete=models.CASCADE)
    Descripcion= models.CharField(max_length=20)
    Area= models.ForeignKey(Areas, on_delete=models.CASCADE)
    Piso= models.IntegerField()
    Observacion = models.TextField(max_length=30)

    def __str__(self):
        return self.serial






