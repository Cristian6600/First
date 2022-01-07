from django.contrib import admin
from .models import Dotacion, User, Talla, Entrega
from import_export import resources
from django.apps import apps
from import_export.admin import ImportExportModelAdmin
from django.db import models
import tablib
import collections

class DotacionResource(resources.ModelResource):
    def __init__(self):
        super(DotacionResource, self).__init__()
        # Obtenga todos los campos en el modelo Libro en la aplicación de tablas, cambie las tablas de acuerdo con su aplicación
        field_list = apps.get_model('dotacion', 'Dotacion')._meta.fields
        self.vname_dict = {}
        self.fkey = []
        for i in field_list:
            self.vname_dict[i.name] = i.verbose_name    # Obtenga el verbose_name de todos los campos y guárdelos en el diccionario
            if(isinstance(i, models.ForeignKey)):
                self.fkey.append(i.name)    # Obtenga los nombres de todos los campos ForeignKey almacenados en la lista

    def export(self, queryset=None, *args, **kwargs):
        self.before_export(queryset, *args, **kwargs)

        if queryset is None:
            queryset = self.get_queryset()

        headers = self.get_export_headers()
        data = tablib.Dataset(headers=headers)

        # Obtener la posición de todos los nombres de claves externas en los encabezados
        fk_index = {}
        for fk in self.fkey:
            fk_index[fk] = headers.index(fk)

        iterable = queryset
        for obj in iterable:
            # Obtenga los datos de origen para exportar, donde export_resource devuelve una lista para una fácil modificación. Reemplazado por el valor de la clave externa
            res = self.export_resource(obj)
            """
                         Aquí está la clave, obtenga el objeto correspondiente del valor del propietario al Usuario e intercepte el nombre de usuario legible,
                         Aquí está get, por lo que el nombre de usuario debe ser único en el modelo de usuario
            """
            res[fk_index['Producto']] = User.objects.get(id=res[fk_index['Producto']]).username
            data.append(res)
        self.after_export(queryset, data, *args, **kwargs)
        return data

    def before_import(self, dataset, using_transactions, dry_run, **kwargs):
        dict = []
        for row in dataset.dict:
            tmp = collections.OrderedDict()
            Dotacion = Dotacion.objects.all()
            for item in row:
                if item == 'Producto':
                    """
                                         Aquí está la clave, encuentre la identificación correspondiente en la tabla Usuario a través del nombre legible y agréguela a los datos importados
                    """
                    tmp[item] = User.objects.get(username=row[item]).id
                else:
                    tmp[item] = row[item]
            """
                         La clave aquí es comparar los datos. Si los datos son los mismos, agregue la identificación original en la tabla del Libro a los datos que se importarán.
                         Esto no agregará los mismos datos que el original, similar al método create_or_update
            """
            for Dotacion in Dotacion:
                if row['name'] == Dotacion.name:
                    tmp['id'] = Dotacion.id
            dict.append(tmp)
        dataset.dict = dict
        return dataset

    class Meta:
        model = Dotacion

class DotacionAdmin(ImportExportModelAdmin):
    resource_class = DotacionResource

class DotacionAdmin(ImportExportModelAdmin):
    resource_class = DotacionResource
    list_display = ['Producto', 'Talla', 'Sucursal', 'cantidad', 'Estado']
    list_filter = ('Producto', 'Talla', 'Sucursal', 'cantidad', 'Estado' )
    search_fields = ['cantidad']

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    list_display = ['username']
    
class EntregaAdmin(ImportExportModelAdmin):
    list_display = ('id', 't_dotacion', 'sucursal')

admin.site.register(Dotacion, DotacionAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(Talla)
admin.site.register(Entrega, EntregaAdmin)