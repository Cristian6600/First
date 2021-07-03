from django.contrib import admin
admin.site.site_header = "Firstsource"
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import m_solicitud, Clasificacion, Proveedor, Sucursal, Estado, pedido_papeleria, Cecos, rep_Costos

class m_solicitudAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    model = m_solicitud
    list_per_page = 12
    

    fieldsets = [
        ('Fecha de solicitud',  
        {'fields': ['f_ingreso', 'f_pago', 'f_contabilidad']}),

        ('Gestion', 
        {'fields': ['Clasificacion', 'proveedor', 'Servicio', 'Sucursal','Compañia','Ceco']}),


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
        'f_ingreso',
        'Servicio',
        'Compañia'
    )

    date_hierarchy = 'f_ingreso'

class ProveedorAdmin(ImportExportModelAdmin, admin.ModelAdmin):   

    list_display = (
        'Nit',
        'Proveedores',

    )
        
    search_fields = (
        'Nit',
        'Proveedores',
    )

class CecosAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    list_display = (
        'id',
        'Nom_ceco',
    )


admin.site.register(m_solicitud, m_solicitudAdmin)
admin.site.register(Clasificacion)
admin.site.register(Proveedor, ProveedorAdmin)
admin.site.register(Sucursal)
admin.site.register(Estado)
admin.site.register(Cecos, CecosAdmin)
admin.site.register(pedido_papeleria)



