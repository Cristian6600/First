from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    View,
)
from applications.M_solicitud.models import m_solicitud
from .forms import m_solicitudForm

class ArticleListView(ListView):

    model = m_solicitud
    template_name = 'polls/index.html'  # if pagination is desired
    context_object_name = 'lista'
