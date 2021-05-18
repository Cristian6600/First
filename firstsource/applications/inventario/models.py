from django.db import models
from applications.users.models import User


class Marcas(models.Model):
    marca = models.CharField(max_length=18)
    modelo =models.CharField(max_length=15)

    def __str__(self):
        return self.marca


class Inventario(models.Model):
    Serial = models.CharField(max_length=30)
    Producto = models.CharField(max_length=20,)
    Marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    Estado = models.BooleanField(default=False)
    Ubicacion = models.CharField(max_length=18)
    Observacion = models.TextField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.Serial






