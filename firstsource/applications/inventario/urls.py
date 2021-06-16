from django.urls import path

from . import views

app_name = "inventario_app"

urlpatterns = [
    path('Listar-todo-inventario/', views.ListAllInventario.as_view()),
    path('Buscar-inventario/', views.ListInventarioBykword.as_view()),
    path('Ver-inventario/<pk>', views.InventarioDetailView.as_view()),
    path('add-inventario/', views.InventarioCreateView.as_view()),

    ]