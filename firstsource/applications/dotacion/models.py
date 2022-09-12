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
    promedio = models.IntegerField()

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

    cantidad = models.IntegerField()

    def __str__(self):
        return str(self.t_dotacion) 

    @property
    def descuento(self):
        return self.cantidad

    def save(self, *args, **kwargs):
        self.t_dotacion.cantidad =  self.descuento

        self.t_dotacion.save()

        super(Entrega, self).save(*args, **kwargs)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    nit = models.CharField(max_length=15)
    telefono = models.IntegerField()
    correo = models.EmailField()

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=15)
    fecha = models.DateField(blank=True, null=True)
    producto = models.ForeignKey(Dotacion, on_delete= models.CASCADE)
    valor_unidad = models.IntegerField()
    cantidad = models.IntegerField()
    total = models.IntegerField(blank=True, null=True)

    @property
    def promedio_prenda(self):
        return self.valor_unidad

    @property
    def valor_total(self):
        return self.valor_unidad * self.cantidad

    def save(self, *args, **kwargs):
        self.total =  self.valor_total
        self.producto.promedio = self.promedio_prenda

        self.producto.save()    
        super(Factura, self).save(*args, **kwargs)