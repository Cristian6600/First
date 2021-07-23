from django.db import models
from applications.M_solicitud.models import Sucursal

class Talla(models.Model):

    talla = models.CharField(primary_key= True, max_length = 5)

    def __str__(self):
        return self.talla

class User(models.Model):

    username = models.CharField(max_length=25, unique=True, verbose_name='Producto')
     
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Ropa'
        verbose_name_plural = 'Ropa'

class Dotacion(models.Model):
    Producto = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name = 'Producto')
    Talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.Producto)

    class Meta:
        verbose_name = 'Dotacion'
        verbose_name_plural = 'Dotacion'