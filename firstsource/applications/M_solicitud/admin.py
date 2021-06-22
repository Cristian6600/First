from django.contrib import admin
admin.site.site_header = "Firstsource"
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import m_solicitud, Clasificacion, Proveedor, Sucursal, Estado, pedido_papeleria, Cecos, rep_conta, rep_Costos, Prov_cont

class m_solicitudAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = m_solicitud
    list_per_page = 12

    fieldsets = [
        ('Fecha de solicitud',  
        {'fields': ['f_ingreso', 'f_pago', 'f_contabilidad']}),

        ('Gestion', 
        {'fields': ['Clasificacion', 'proveedor', 'Servicio', 'Sucursal','Compañia','Ceco']}),

        ('Ingressar Novedad', 
        {'fields': ['Novedades']}),

        ('Gasto Producto', {'fields': ['V_gasto', 'iva', 'V_total']}),
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
        'Compañia',
    )
    
    list_filter = (
        'f_ingreso',
        'f_pago',
        'f_contabilidad',
    )

    search_fields = (
        'proveedor',
        'Servicio',
        'Compañia'
    )
class rep_contaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = rep_conta
    list_per_page = 12

    fieldsets = [
        ('Reporte',  
        {'fields': ['N_factura', 'Proveedor', 'Fecha']}),

        ('Costos', 
        {'fields': ['Valor', 'Iva', 'Va_total']}),

        ('Centro de costos', 
        {'fields': ['Ceco']}),

        ('Observacion', {'fields': ['Observaciones']}),
    ]

    list_display = (
        'N_factura',
        'Proveedor',
        'Fecha',
        'Valor',
        'Iva',
        'Va_total',
        'Ceco',
    )
    search_fields = (
        'N_factura',
        'Ceco',
    )

    list_filter = (
        'Fecha',
    )

class rep_CostosAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = rep_conta
    list_per_page = 12

    fieldsets = [
        ('Reporte',  
        {'fields': ['N_factura', 'Proveedor', 'Fecha']}),

        ('Costos', 
        {'fields': ['Valor', 'Iva', 'Va_total']}),

        ('Centro de costos', 
        {'fields': ['Ceco']}),

        ('Observacion', {'fields': ['Observaciones']}),
    ]

    list_display = (
        'N_factura',
        'Proveedor',
        'Fecha',
        'Valor',
        'Iva',
        'Va_total',
        'Ceco',

    )

    search_fields = (
        'N_factura',
        'Ceco',
    )

    list_filter = (
        'Fecha',
    )


admin.site.register(m_solicitud, m_solicitudAdmin)
admin.site.register(Clasificacion)
admin.site.register(Proveedor)
admin.site.register(Sucursal)
admin.site.register(Estado)
admin.site.register(Cecos)
admin.site.register(pedido_papeleria)
admin.site.register(rep_conta, rep_contaAdmin)
admin.site.register(rep_Costos, rep_CostosAdmin)
admin.site.register(Prov_cont)

