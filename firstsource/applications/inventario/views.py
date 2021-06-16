from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import Inventario
from django.urls import reverse_lazy, reverse

from django.views.generic import(
    ListView,
    DetailView,
    CreateView,
)

class ListAllInventario(ListView):
    template_name = 'inventario/list.html'
    model = Inventario
    paginate_by = 2
    context_object_name = 'lista'

class ListInventarioBykword(ListView):
    """Lista inventario por palabra clave """
    template_name = 'inventario/Buscar.html'
    model = Inventario
    context_object_name = 'inventario'

    def get_queryset(self):
        print('**************')
        palabra_clave = self.request.GET.get("kword", '')
        lista = Inventario.objects.filter(
            Serial= palabra_clave
        )
        print('lista resultado:', lista)
        return lista

class InventarioDetailView(DetailView):
    model = Inventario
    template_name = "inventario/detail_inventario.html"


class InventarioCreateView(LoginRequiredMixin, CreateView):
    template_name = "inventario/add.html"
    login_url = reverse_lazy('users_app:user-login')
    model = Inventario
    fields = ('__all__')
    success_url = '.'
