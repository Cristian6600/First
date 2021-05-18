from django.contrib import admin

from . models import Inventario, Marcas, Licencia

class InventarioAdmin(admin.ModelAdmin):
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
        'Marca',
    )
    search_fields = ['Serial']
          

admin.site.register(Inventario, InventarioAdmin)
admin.site.register(Marcas)
admin.site.register(Licencia)
