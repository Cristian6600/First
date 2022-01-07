from django.db import models
from applications.M_solicitud.models import Sucursal
from applications.users.models import Areas

    

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

    ESTADOS = [
        ('Entregado', 'ENTREGADO'),
        ('Disponible ', 'DISPONIBLE '),
        ('Utilizado ', 'UTILIZADO '),

    ]  

    Producto = models.ForeignKey(User, on_delete=models.CASCADE)
    Talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    Estado = models.CharField(max_length= 12, choices = ESTADOS)

    def __str__(self):
        return str(self.Producto) + '-' + str(self.Talla)

    class Meta:
        verbose_name = 'Dotacion'
        verbose_name_plural = 'Dotacion'

class Entrega(models.Model):

    t_dotacion = models.ForeignKey(
        Dotacion,
        on_delete=models.CASCADE)

    area = models.ForeignKey(
        Areas,
        on_delete=models.CASCADE)

    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE)

    def __str__(self):
        return str(self.t_dotacion) 

    def save(self, *args, **kwargs):
        self.t_dotacion.cantidad =  self.t_dotacion.cantidad - 1

        self.t_dotacion.save()

        super(Entrega, self).save(*args, **kwargs)


