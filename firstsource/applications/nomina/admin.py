from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from import_export.fields import Field

# class NominaResource(resources.ModelResource):
#     myfield = Field(column_name='myfield')

#     class Nomina:
#         model = Nomina
#         exclude = ('id')
    
# class NominaAdmin(ImportExportModelAdmin, admin.ModelAdmin):

#      model = Nomina
#      list_per_page = 12

#      list_display = (
#          'Fecha',
#          'Cta',
#          'D_C',
#          'Identificacion',
#          'Nombre',
#          'Codigo',
#          'Nombre_CC',
#          'Concepto',
#          'Valor',

#      )

#      list_filter = (
#          'Fecha',
#          'Concepto',
#      )
#      search_fields = ('Fecha', 'Identificacion', 'Nombre')


# class SeguridadResource(resources.ModelResource):
#     myfield = Field(column_name='myfield')

#     class Seguridad:
#         model = Seguridad
#         exclude = ('id')
     
# class SeguridadAdmin(ImportExportModelAdmin, admin.ModelAdmin):  

#      model = Seguridad
#      list_per_page = 12  

#      list_display = (
#          'Fecha',
#          'Identificacion',
#          'Provision',
#          'Cta',
#          'D_C',
#          'Valor',
#          'Nombre',
#          'Centro_Costo',
#          'Concepto',
#      )
#      list_filter = (
#          'D_C',
#          'Concepto',
#      )
#      search_fields = ('Identificacion', 'D_C', 'Centro_Costo', 'Concepto',)

    

# admin.site.register(Nomina, NominaAdmin)
# admin.site.register(Seguridad, SeguridadAdmin)