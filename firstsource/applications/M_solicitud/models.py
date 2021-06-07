from django.db import models
from django.db.models.fields import CharField, TextField

class Estado(models.Model):
    ESTADO_CHOICES = [
      ('ESPER',  'Espera de aprobacion'),
      ('APRO', 'Aprobado'),
      ('RECHA', 'Rechazado'),
        
    ]  
    Estado = models.CharField(max_length=6,
    choices=ESTADO_CHOICES,
    blank=True)

    Observaciones = models.TextField(max_length=100, blank=True)
    Fecha = models.DateTimeField(blank=True)

class Clasificacion(models.Model):
    Clasificaciones= models.CharField(max_length=30, primary_key=True)

    def __str__(self):
        return self.Clasificaciones

class Proveedor(models.Model):
    Proveedores = models.CharField(max_length=30, primary_key=True)

    class Meta:
        verbose_name = "Proveedor"
        verbose_name_plural = "Proveedores"

    def __str__(self):
        return self.Proveedores

class Sucursal(models.Model):
    Sucursal = models.CharField(max_length=30, primary_key=True,)

    def __str__(self):
        return self.Sucursal
       

class Cecos(models.Model):
    Ceco = models.CharField(max_length=50, primary_key=True)
    Nom_ceco = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = "Ceco"
        verbose_name_plural = "Cecos"


    def __str__(self):
        return self.Ceco

class m_solicitud(models.Model):
    com_CHOICES = [
      ('Firstsource', 'Firstsource'),
      ('TSE', 'TSE'),
      ('CP', 'CP'),              
    ]  

    f_ingreso= models.DateField()
    f_pago = models.DateField()
    f_contabilidad = models.DateField()
    
    Clasificacion = models.ForeignKey(
        Clasificacion,
        on_delete=models.CASCADE
    )

    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    Servicio = models.CharField(max_length=60, blank=True)
      
    Sucursal = models.ManyToManyField(Sucursal)
    Compañia = models.CharField(max_length=20, choices=com_CHOICES, blank= True)
    Ceco = models.ForeignKey(Cecos, on_delete=models.CASCADE, null= True)
    Novedades = models.TextField(max_length=150, blank=True)
    V_gasto = models.IntegerField() 
    iva = models.IntegerField()
    V_total = models.IntegerField()

    class Meta:
        verbose_name = "Matriz de compra"
        verbose_name_plural = "Matriz de compras"
    

    def __str__(self):
        return "%s %s %s" % (self.Clasificacion, self.proveedor, self.V_gasto)

class pedido_papeleria(models.Model):
     ti_pape = models.CharField('tipo de papeleria', max_length=30)
     can_pape = models.IntegerField('cantidad papeleria')
     Estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

     class Meta:
        verbose_name = "Pedido de papeleria"
        verbose_name_plural = "Pedido de papeleria"



