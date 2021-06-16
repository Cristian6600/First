from django.db import models
from django.db.models.aggregates import Max
from django.db.models.fields import CharField, DateField, IntegerField


# Create your models here.
class Cargue (models.Model):
    Consecutivo = models.IntegerField()
    Identificacion = models.CharField(max_length=15)
    Nom_completo = models.CharField(max_length=60)
    Dias = models.CharField(max_length=2)
    CODIGO_CC = models.CharField(max_length=10)
    Centro_Costo = models.CharField(max_length=40)
    Sueldo = models.DecimalField(max_digits=12, decimal_places=3)

    Aux_transporte  = models.DecimalField(max_digits=12, decimal_places=3)
    Aux_ex_transporte = models.DecimalField(max_digits=12, decimal_places=3)
    Aux_Rodamiento = models.DecimalField(max_digits=12, decimal_places=3)
    G_transporte = models.DecimalField(max_digits=12, decimal_places=3)
    Ajuste_roda_pos = models.DecimalField(max_digits=12, decimal_places=3)

    Ajuste_roda_neg = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad1 = models.IntegerField()

    Hora_ex_dom_fes_sin_com = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad2 = models.IntegerField()

    Hora_ex_dom_fes_con_com = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad3 = models.IntegerField()

    hora_ex_diur = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad4 = models.IntegerField()

    Hora_ex_noc = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad5 = models.IntegerField()

    Recargo_noc = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad6 = models.IntegerField()
    
    Recargo_noc_fes = models.DecimalField(max_digits=12, decimal_places=3)
    Inactividad = models.DecimalField(max_digits=12, decimal_places=3)
    Retroactivo = models.DecimalField(max_digits=12, decimal_places=3)
    Vacaciones = models.DecimalField(max_digits=12, decimal_places=3)
    Vacaciones_plata = models.DecimalField(max_digits=12, decimal_places=3)
    Comisiones = models.DecimalField(max_digits=12, decimal_places=3)
    Prima_legal = models.DecimalField(max_digits=12, decimal_places=3)
    Cuota_sos_lec = models.DecimalField(max_digits=12, decimal_places=3)
    Sal_integral = models.DecimalField(max_digits=12, decimal_places=3)

    in_cesantias = models.DecimalField(max_digits=12, decimal_places=3)
    Cantidad7 = models.IntegerField()

    Ajustes_red_noc = models.DecimalField(max_digits=12, decimal_places=3)
    cuo_sos_produ = models.DecimalField(max_digits=12, decimal_places=3)
    Entregas_efec = models.DecimalField(max_digits=12, decimal_places=3)
    Bonificacion = models.DecimalField(max_digits=12, decimal_places=3)
    Prima_ex_lega = models.DecimalField(max_digits=12, decimal_places=3)
    Ajus_prima = models.DecimalField(max_digits=12, decimal_places=3)
    Aux_alimentacion = models.DecimalField(max_digits=12, decimal_places=3)

    Apor_salud = models.DecimalField(max_digits=12, decimal_places=3)
    Apor_Pension = models.DecimalField(max_digits=12, decimal_places=3)
    Fon_solidaridad = models.DecimalField(max_digits=12, decimal_places=3)
    Retencion_fuen = models.DecimalField(max_digits=12, decimal_places=3)
    O_descuentos = models.DecimalField(max_digits=12, decimal_places=3)
    Des_prima = models.DecimalField(max_digits=12, decimal_places=3)
    F_E_Beneficiar = models.DecimalField(max_digits=12, decimal_places=3)
    A_inactividad = models.DecimalField(max_digits=12, decimal_places=3)
    D_cred_f_e_beneficiar = models.DecimalField(max_digits=12, decimal_places=3)
    Poliza_vida = models.DecimalField(max_digits=12, decimal_places=3)
    Dto_lentes = models.DecimalField(max_digits=12, decimal_places=3)
    D_Aportes_año = models.DecimalField(max_digits=12, decimal_places=3)

    Tot_neto_pa = models.DecimalField(max_digits=12, decimal_places=3)
    Tot_neto_pa_com =models.DecimalField(max_digits=12, decimal_places=3)

    Banco = models.CharField(max_length=15)
    Cuen_bancaria = models.CharField(max_length=15)
    
    Total_devengado = models.DecimalField(max_digits=12, decimal_places=3, blank=True)
    
    Total_descuentos = models.DecimalField(max_digits=12, decimal_places=3, null=True, blank=True)  
    
    @property
    def Descuentos(self):
       return (self.Apor_salud + self.Apor_Pension + self.Fon_solidaridad + self.Retencion_fuen +
       self.O_descuentos + self.Des_prima + self.F_E_Beneficiar + self.A_inactividad + 
       self.D_cred_f_e_beneficiar + self.Poliza_vida + self.Dto_lentes + self.D_Aportes_año )

    def save(self):
        self.Total_descuentos = self.Descuentos
        super (Cargue, self).save()

    @property
    def devengado(self):
       return (self.Sueldo + self.Aux_transporte + self.Aux_ex_transporte +
       self.Aux_Rodamiento + self.G_transporte + self.Ajuste_roda_pos + 
       self.Ajuste_roda_neg + self.Hora_ex_dom_fes_sin_com + self.Hora_ex_dom_fes_con_com + 
       self.hora_ex_diur + self.Hora_ex_noc + self.Recargo_noc + self.Inactividad + 
       self.Retroactivo + self.Vacaciones + self.Vacaciones_plata+ self.Comisiones +
       self.Prima_legal + self.Cuota_sos_lec + self.Sal_integral + self.in_cesantias + 
       self.Ajustes_red_noc + self.cuo_sos_produ + self.Entregas_efec +
       self.Bonificacion + self.Prima_ex_lega + self.Ajus_prima + self.Aux_alimentacion)

    def save(self):
        self.Total_devengado = self.devengado
        super (Cargue, self).save()

    class Meta:
        verbose_name = "Nomina "
        verbose_name_plural = "Nomina"
 

    def __str__(self):
       return self.Nom_completo

class Seguridad (models.Model):
    Fecha = models.DateField()
    Identificacion = models.CharField(max_length = 15 )
    Provision = models.CharField(max_length=20)
    Cta = models.IntegerField()
    D_C = models.CharField(max_length=1)
    Valor = models.DecimalField(max_digits=12, decimal_places=0)
    Nombre = models.CharField(max_length=60)
    Centro_Costo = models.CharField(max_length=20)
    Concepto = models.CharField(max_length=15)

    class Meta:
        verbose_name = "Seguridad Social"
        verbose_name_plural = "Seguridad Social"

    def __str__(self):
       return self.Nombre








