from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Inventario, Marcas, Licencia, Hardware, inmobiliario, Articulo

class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario

class InventarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'Serial',
        'Producto',
        'Marca',
        'Estado',
        'Ubicacion',
        'Observacion',
        'usuario',
    )
    list_filter = (
        'Serial',
        'Producto',
        'Marca',
        'Estado',
        'Ubicacion',
    )
    search_fields = ['Serial']

    resources_class = InventarioResource

class inmobiliarioAdmin(admin.ModelAdmin):
    list_display = (
        'serial',
        'Articulo',
        'Descripcion',
        'Area',
        'Piso',
    )



    
admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Marcas)
admin.site.register(Licencia)
admin.site.register(Hardware)
admin.site.register(inmobiliario, inmobiliarioAdmin)
admin.site.register(Articulo)

