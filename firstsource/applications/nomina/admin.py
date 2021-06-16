from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from . models import Cargue, Seguridad
from import_export.fields import Field

class CargueResource(resources.ModelResource):
    myfield = Field(column_name='myfield')

    class Cargue:
        model = Cargue
        exclude = ('id')
    
class CargueAdmin(ImportExportModelAdmin, admin.ModelAdmin):

     model = Cargue
     list_per_page = 12

     list_display = (
         'Identificacion',
         'Nom_completo',
         'CODIGO_CC',
         'Centro_Costo',
         'Sueldo',
         'Total_devengado',
         #'Total_descuentos',
     )

     list_filter = (
         'Centro_Costo',
     )
     search_fields = ('Identificacion', 'CODIGO_CC')


class SeguridadResource(resources.ModelResource):
    myfield = Field(column_name='myfield')

    class Seguridad:
        model = Seguridad
        exclude = ('id')
     
class SeguridadAdmin(ImportExportModelAdmin, admin.ModelAdmin):  

     model = Seguridad
     list_per_page = 12  

     list_display = (
         'Fecha',
         'Identificacion',
         'Provision',
         'Cta',
         'D_C',
         'Valor',
         'Nombre',
         'Centro_Costo',
         'Concepto',
     )
     list_filter = (
         'D_C',
         'Concepto',
     )
     search_fields = ('Identificacion', 'D_C', 'Centro_Costo', 'Concepto',)

    

admin.site.register(Cargue, CargueAdmin)
admin.site.register(Seguridad, SeguridadAdmin)