from django.contrib import admin
admin.site.site_header = "Firstsource"
from import_export.admin import ImportExportModelAdmin
from import_export import resources


from . models import m_solicitud, Clasificacion, Proveedor, Sucursal, Estado, pedido_papeleria, Seco
# Register your models here.
class m_solicitudAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    fieldsets = [
        ('Fecha de solicitud',  
        {'fields': ['f_ingreso', 'f_pago', 'f_contabilidad']}),

        ('Gestion', 
        {'fields': ['Clasificacion', 'proveedor', 'Servicio', 'Sucursal','Compañia','Seco']}),

        ('Ingressar Novedad', 
        {'fields': ['Novedades']}),

        ('Gasto', {'fields': ['V_gasto', 'iva', 'V_total']}),
    ]
    
    list_display = (
        'f_ingreso',
        'f_pago',
        'f_contabilidad',
        'Clasificacion',
        'proveedor',
        'V_gasto',
        'iva',
        'V_total',
    )
admin.site.register(m_solicitud, m_solicitudAdmin)
admin.site.register(Clasificacion)
admin.site.register(Proveedor)
admin.site.register(Sucursal)
admin.site.register(Estado)
admin.site.register(Seco)
admin.site.register(pedido_papeleria)

