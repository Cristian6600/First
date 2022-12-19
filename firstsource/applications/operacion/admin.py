from django.contrib import admin
from .models import Facturacion, Detalle
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.utils.translation import gettext_lazy as _

class AuthDecadeBornListFilter(Facturacion):
    
    def lookups(self, request, model_admin):
        if request.user.is_superuser:
            return super().lookups(request, model_admin)

    def queryset(self, request, queryset):
        if request.user.is_superuser:
            return super().queryset(request, queryset)

class DetalleResource(resources.ModelResource):
    class Meta:
        model = Detalle
        fields = ('id__fecha','id__tipo_servicio','id__sucursal', 'id__placa', 'id__tipo_vehiculo', 'id__entregas', 'id__visitas', 'id', 'factura_vehiculo', 'efectividad', 'valor_auxiliar')
        export_order = ('id__fecha','id__tipo_servicio','id__sucursal', 'id__placa', 'id__tipo_vehiculo', 'id__entregas', 'id', 'factura_vehiculo', 'efectividad', 'valor_auxiliar')

class DetalleAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("fecha","tipo_servicio","sucursal", "placa","tipo_vehiculo","entregas", 'visita', "factura_vehiculo", 'os', 'efectividad', 'valor_auxiliars')#
    resource_class = DetalleResource
    list_editable = ('os',)
    date_hierarchy = 'id__fecha'
    list_filter = ('id__sucursal', 'id__tipo_vehiculo')
    
    @admin.display(empty_value='???')
    def fecha(self, obj):
        return obj.id.fecha
    
    @admin.display(empty_value='???')
    def tipo_servicio(self, obj):
        return obj.id.tipo_servicio

    @admin.display(empty_value='???')
    def sucursal(self, obj):
        return obj.id.sucursal

    @admin.display(empty_value='???')
    def placa(self, obj):
        return obj.id.placa

    @admin.display(empty_value='???')
    def tipo_vehiculo(self, obj):
        return obj.id.tipo_vehiculo

    @admin.display(empty_value='???')
    def entregas(self, obj):
        return obj.id.entregas   
    
    @admin.display(empty_value='???')
    def visita(self, obj):
        return obj.id.visitas

class FacturaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('fecha','tipo_servicio','sucursal', 'placa', 'tipo_vehiculo','entregas' ,'visitas')
    
admin.site.register(Facturacion, FacturaAdmin)
admin.site.register(Detalle, DetalleAdmin)