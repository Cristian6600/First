from django.db import models
from django.db.models.fields import BooleanField, CharField
from applications.users.models import User, Areas
from applications.M_solicitud.models import Sucursal
from django.conf import settings 

class Marcas(models.Model):
    marca = models.CharField(max_length=18, primary_key=True, unique=True)
    

    def __str__(self):
        return self.marca 

class Licencia(models.Model):
    serial = models.CharField(max_length=45, primary_key=True, unique=True)
    software = models.CharField(max_length=25)

    def __str__(self):
        return self.serial

class Hardware(models.Model):
    Hardware = models.CharField(max_length=30, primary_key=True, unique=True) 

    class Meta:
        verbose_name = "Hardware"
        verbose_name_plural = "Hardware"

    def __str__(self):
        return self.Hardware


class Inventario(models.Model):
    Serial = models.CharField(max_length=30)
    Producto = models.ForeignKey(Hardware, on_delete=models.CASCADE, verbose_name= 'Hardware')
    Marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    Modelo = models.CharField(max_length=30)
    Estado = models.BooleanField(default=False)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    Ubicacion = models.ForeignKey(Areas, on_delete=models.CASCADE)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    Licencia = models.ManyToManyField(Licencia)
    Observacion = models.TextField(max_length=250)
    ip = models.CharField(max_length=20, blank=True)
    Mac = models.CharField(max_length=20)
    Ram = models.CharField(max_length=6, blank=True)
    Disco = models.CharField(max_length=30, blank=True)
    Procesador = models.CharField(max_length=15, blank=True)
    Usb = models.BooleanField(default=False, blank=True)
    Hdmi = models.BooleanField(default=False, blank=True)
    Vga = models.BooleanField(default=False, blank=True)
    Bloq_ex = BooleanField(default=False, blank=True, verbose_name='Bloqueo de extraibles')
    bloq_pa= BooleanField(default=False, blank=True, verbose_name='Bloqueo de panel de control')
    #in_cont = models.CharField(max_length=2, verbose_name='Intento contraseñas', blank=True)

    

    class Meta:
        verbose_name = "Inventario"
        verbose_name_plural = "Inventario Tecnologia"



    
    def __str__(self):
        return self.Serial


class Articulo(models.Model):
    Articulo = models.CharField(max_length=30, primary_key=True, unique=True)

    def __str__(self):
        return self.Articulo


class inmobiliario(models.Model):

    Se_CHOICES = [
      ('Cali', 'Cali'),
      ('Barranquilla', 'Barranquilla'),
      ('Bucaramanga', 'Bucaramanga'),
      ('Bogota', 'Bogota'),
      ('Cartagena', 'Cartagena'),
      ('Medelin', 'Medelin'),
      ('Eje cafetero', 'Eje cafetero'),
                
    ]  
    serial= models.CharField(max_length=20)
    Articulo= models.ForeignKey(Articulo, on_delete=models.CASCADE)
    Descripcion= models.CharField(max_length=20)
    Sede = models.CharField(max_length=20, choices=Se_CHOICES)
    Area= models.ForeignKey(Areas, on_delete=models.CASCADE)
    Piso= models.IntegerField()
    Observacion = models.TextField(max_length=30)
    estado = models.BooleanField(default = True)
    responsable = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE, 
        null=True, 
    )

    class Meta:
        verbose_name = "Inventario Inmobiliario "
        verbose_name_plural = "Inventario Inmobiliarios"
    

    def __str__(self):
        return self.serial






