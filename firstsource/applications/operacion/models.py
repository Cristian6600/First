from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

class Facturacion(models.Model):
    CIUDAD = (
        ('BOGOTA', 'BOGOTA'),
        ('MEDELLIN', 'MEDELLIN'),
        ('CALI', 'CALI'),
        ('BARRANQUILLA', 'BARRANQUILLA'),
        ('CARTAGENA', 'CARTAGENA'),
        ('PEREIRA', 'PEREIRA'),
        ('BUCARAMANGA', 'BUCARAMANGA'),
    )
    TIPOVEICULO = (
        ('MOTORIZADO', 'MOTORIZADO'),
        ('CARRY', 'CARRY')
    )
    fecha = models.DateField()
    tipo_servicio = models.CharField(max_length=50)
    sucursal = models.CharField(max_length=70, choices=CIUDAD)
    placa = models.CharField(max_length=10)
    tipo_vehiculo= models.CharField(max_length=40, choices=TIPOVEICULO)
    entregas = models.IntegerField(verbose_name='Unidades cargue')
    visitas = models.IntegerField(verbose_name='Total entregado')

class Detalle(models.Model):
    
    id = models.OneToOneField(
        Facturacion, primary_key=True, 
        on_delete=models.CASCADE,
        )
    factura_vehiculo = models.IntegerField(verbose_name="FACTURA POR VEHICULO", blank=True, null=True)
    os = models.IntegerField(blank=True, null=True)
    efectividad = models.CharField(max_length=25, verbose_name='porcentaje de efectividad')
    valor_auxiliar = models.IntegerField(blank=True, null=True)

    def valor_auxiliars(self):
        return '$' + str(self.valor_auxiliar)

    def save(self, *args, **kwargs):
        ####### Da valor solo a CARRY #########

        if self.id.tipo_vehiculo == 'CARRY' and self.id.sucursal == "BOGOTA":
            self.valor_auxiliar = 0

        elif self.id.tipo_vehiculo == 'CARRY':
            self.valor_auxiliar = 59000
        else:
            self.valor_auxiliar = 0

        ######## calcular porcentaje ##########

        if self.id.entregas == 0:
            self.efectividad = "0%"

        elif self.id.entregas != 0:
            var = self.id.visitas / self.id.entregas * 100 
            (var2) = int(var) 
            (b) = round(int(var2))
            self.efectividad = str(b) + "%"

        ######## DA VALOR FIFRENTE CUANDO SON MAYORES, MENORES, O EXCEPCIONES ########

        if self.id.sucursal == "BOGOTA" and self.id.tipo_vehiculo == "MOTORIZADO":
            self.factura_vehiculo = 60000

        elif self.id.sucursal == "BOGOTA" and self.id.tipo_vehiculo == "CARRY":
            self.factura_vehiculo = 240000
        ####
        elif self.id.entregas <= 28 and self.id.tipo_vehiculo == "MOTORIZADO":
            self.factura_vehiculo = 138292

        elif self.id.entregas > 28 and self.id.tipo_vehiculo == "MOTORIZADO":
            self.factura_vehiculo = self.id.entregas * 4939

        elif self.id.entregas <= 40 and self.id.tipo_vehiculo == "CARRY":
            self.factura_vehiculo = 197560
        
        elif self.id.entregas > 40 and self.id.tipo_vehiculo == "CARRY":
            self.factura_vehiculo = self.id.entregas * 4939
        
        super(Detalle, self).save(*args, **kwargs)

@receiver(post_save, sender=Facturacion)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Detalle.objects.create(id=instance)


# @receiver(post_save, sender=Facturacion)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()