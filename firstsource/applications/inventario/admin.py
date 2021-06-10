from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Inventario, Marcas, Licencia, Hardware, inmobiliario, Articulo

class InventarioResource(resources.ModelResource):
    class Meta:
        model = Inventario

class InventarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    fieldsets = [
        ('Tecnologia', {'fields': ['Serial', 'Producto', 'Marca', 'Modelo',
         'Estado', 'Sucursal', 'Ubicacion', 'usuario', 'Observacion', 'ip', 'Mac',]}),
        ('Politicas', {'fields': ['Licencia', 'Ram', 'Disco', 'Procesador',
         'Usb', 'Hdmi', 'Vga', 'Bloq_ex', 'bloq_pa']}),
    ]

    list_display = (
        'Serial',
        'Producto',
        'Marca',
        'Sucursal',
        'Estado',
        'Ubicacion',
        'usuario',
        'Observacion',
    )
    list_filter = (
        'Marca',
        'Estado',
        'Ubicacion',
    )
    search_fields = ['Serial']

    resources_class = InventarioResource

class MarcasAdmin(admin.ModelAdmin):
    list_filter = ('marca',)

class inmobiliarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = (
        'serial',
        'Articulo',
        'Descripcion',
        'Sede',
        'Area',
        'Piso',
    )
    list_filter = (
        'Sede',
        
    )




admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Marcas, MarcasAdmin)
admin.site.register(Licencia)
admin.site.register(Hardware)
admin.site.register(inmobiliario, inmobiliarioAdmin)
admin.site.register(Articulo)

