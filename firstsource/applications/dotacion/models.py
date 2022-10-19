import re
from tabnanny import verbose
from django.db import models
from applications.M_solicitud.models import Sucursal, Cecos
from applications.users.models import Areas

class Tipo(models.Model):
    categoria = models.CharField(max_length=35)

    def __str__(self):
        return self.categoria

class Talla(models.Model):

    talla = models.CharField(primary_key= True, max_length = 5)

    def __str__(self):
        return self.talla

class User(models.Model):

    username = models.CharField(max_length=25, unique=True, verbose_name='Producto')
    categoria = models.ForeignKey(Tipo, on_delete=models.CASCADE, blank=True, null=True)
     
    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categoria'

class Dotacion(models.Model):

    Producto = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='dotacion_ropa')
    Talla = models.ForeignKey(Talla, on_delete=models.CASCADE)
    Sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(verbose_name='stock', default=0)
    stock_usado = models.IntegerField(default=0)
    promedio = models.IntegerField(default=0)
    total_dotacion = models.IntegerField(verbose_name="total disponible", default=0)
    valor_promedio = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.Producto) + '-' + str(self.Talla)

    class Meta:
        verbose_name = 'Dotacion'
        verbose_name_plural = 'Dotacion'
        unique_together = [['Producto', 'Talla']]

    @property
    def total_da(self):
        return (self.cantidad)

    @property
    def total_de(self):
        return (self.stock_usado)

    @property
    def total_d(self):
        return int(self.total_da + self.total_de)

    @property
    def valor_promedios(self):
      return (self.cantidad * self.promedio)

    def save(self, *args, **kwargs):
        self.total_dotacion = self.total_d
        self.valor_promedio = self.valor_promedios

        super(Dotacion, self).save(*args, **kwargs)

class Entrega(models.Model):

    t_dotacion = models.ForeignKey(
        Dotacion,
        on_delete=models.CASCADE)

    ceco = models.ForeignKey(Cecos, on_delete=models.CASCADE, verbose_name='Centro de costos')

    sucursal = models.ForeignKey(
        Sucursal,
        on_delete=models.CASCADE)

    cantidad = models.IntegerField()

    fecha = models.DateField()

    def __str__(self):
        return str(self.t_dotacion) 

    @property
    def descuento(self):
        return self.cantidad

    def save(self, *args, **kwargs):
        self.t_dotacion.cantidad = self.t_dotacion.cantidad - self.descuento

        self.t_dotacion.save()

        super(Entrega, self).save(*args, **kwargs)

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    nit = models.CharField(max_length=15)
    telefono = models.CharField(max_length=12)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Factura(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    numero_factura = models.CharField(max_length=15)
    fecha = models.DateField(blank=True, null=True)
    total_factura = models.IntegerField(blank=True, null=True, default= 0)
    total_unidades = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.numero_factura

    @property
    def promedio_prenda(self):
        return self.valor_unidad

    @property
    def totals(self):
        return int(self.cantidad)

class Producto_factura(models.Model):
    dotacion = models.ForeignKey(Dotacion, on_delete=models.CASCADE, related_name="dotacion_detalle")
    cantidad = models.IntegerField()
    factura = models.ForeignKey(Factura, on_delete=models.CASCADE, related_name="factura_k")
    valor_unidad = models.IntegerField()
    total = models.IntegerField(blank=True, null=True, verbose_name='subtotal')

    @property
    def cantidadd(self):
        return int(self.cantidad)

    @property
    def total_facturad(self):
        return int(self.total)
    
    @property
    def promediof(self):
        return int(self.valor_unidad)

    @property
    def valor_total(self):
        return int(self.valor_unidad * self.cantidad)
    
    def save(self, *args, **kwargs):
        self.total = self.valor_total
        self.dotacion.cantidad = self.dotacion.cantidad + self.cantidadd
        self.dotacion.promedio = self.promediof
        self.dotacion.save() 
        self.factura.total_factura =  self.factura.total_factura + self.total_facturad
        self.factura.total_unidades =  self.factura.total_unidades + self.cantidadd
        self.factura.save()       
        super(Producto_factura, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'detalle'

class Devolucion(models.Model):
    dotacion = models.ForeignKey(Dotacion, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    fecha = models.DateField(auto_now = True)

    @property
    def total_devolucion(self):
        return int(self.cantidad)
        
    def save(self, *args, **kwargs):
        self.dotacion.stock_usado = self.dotacion.stock_usado + self.total_devolucion
        
        self.dotacion.save() 
             
        super(Devolucion, self).save(*args, **kwargs)

