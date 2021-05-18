from django.contrib import admin

from . models import indicador, tipo_indicador

class indicadorAdmin(admin.ModelAdmin):
    list_display = (
        'Periodo',
        'aspectos',
        'solicitud',
        'Año',
        'Porcentage_indicador',
        
        
    )
    list_filter = ('aspectos', 'Año', )
    

    def Porcentage_indicador(self, obj):
        print (obj.solicitud )
        return obj.meta / obj.limite * 100

        

        #return obj.solicitud + ' ' + obj.Area


admin.site.register(indicador, indicadorAdmin)
admin.site.register(tipo_indicador)


