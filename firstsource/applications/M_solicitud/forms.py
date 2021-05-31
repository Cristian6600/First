from django import forms
from django.db.models import fields
from django.forms import widgets

from .models import m_solicitud

class m_solicitudForm(forms.ModeForm):

    model = m_solicitud
    fields = (
        'f_ingreso',
        'f_pago',
        'f_contabilidad',
        'Clasificacion',
        'proveedor',
        'Sucursal',
        'V_gasto',
    )
    widgets = {
        'f_ingreso':forms.DateInput(
            attrs= {
                'placeholder': 'Fecha de Ingreso',
                'class': 'input-group-field'
            }
        ),
    }

