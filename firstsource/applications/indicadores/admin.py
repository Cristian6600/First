from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import indicador, tipo_indicador
from import_export.fields import Field


class indicadorResource(resources.ModelResource):
    full_title = Field()
    class Meta:
        model = indicador
        fields = ('Tipo', 'Periodo', 'aspectos',)

class indicadorAdmin(ImportExportModelAdmin, admin.ModelAdmin):

    fieldsets = [
        (None,               {'fields': ['Tipo', 'Periodo', 'Año', 'meta', 'limite', 'aspectos', 'solicitud']}),
        ('Total', {'fields': ['Porcentaje']}),
    ]


    list_display = (
        'Tipo',
        'Periodo',
        'aspectos',
        'solicitud',
        'Año',
        'Porcentaje',
        
    )
    list_filter = ('aspectos', 'Año', 'Tipo',)
    resources_class = indicadorResource
    
    #def Porcentaje_indicador(self, obj):
     #   print (obj.solicitud )
      #  return obj.meta / obj.limite * 100
      #return obj.solicitud + ' ' + obj.Area

admin.site.register(indicador, indicadorAdmin)
admin.site.register(tipo_indicador)


