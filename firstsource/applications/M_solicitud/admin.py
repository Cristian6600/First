from django.contrib import admin
admin.site.site_header = "Firstsource"


from . models import m_solicitud, Clasificacion, Proveedor, Sucursal, Estado, pedido_papeleria
# Register your models here.
class m_solicitudAdmin(admin.ModelAdmin):
    
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
admin.site.register(pedido_papeleria)

