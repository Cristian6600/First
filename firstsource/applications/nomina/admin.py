from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

from . models import Cargue

class CargueAdmin(ImportExportModelAdmin, admin.ModelAdmin):

     list_display = (
         'Fecha',
         'Identificacion',
         'Descripcion',
         'CODIGO_CC',
         'Cuenta_Contable',
         'Tipo',
         'Valor',
         'Nombre',
         'Concepto',
     )

     class Meta:
        model = Cargue
        exclude = ('id')

     list_filter = (
         'Fecha',
         'CODIGO_CC',
         'Concepto',

     )
     search_fields = ['Identificacion',]

    #  class Meta:
    #        model = Cargue
    #        widgets = {
    #                'Fecha': {'format': '%y.%m.%d'},
    #                }
    


admin.site.register(Cargue, CargueAdmin)

    