from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import AltaVehiculo, Cliente, Vehiculo
from .forms import altaVehiculoForm
from cliente.forms import ClienteForm
from vehiculo.forms import VehiculoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)


class AltaVehiculoCreate(CreateView):
    model = AltaVehiculo
    form_class = altaVehiculoForm
    template_name = 'altaVehiculo/alta_vehiculo_form.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # Guardar AltaVehiculo
        alta_vehiculo = form.save()

        # Crear formularios de Cliente y Vehiculo
        cliente_form = ClienteForm(self.request.POST)
        vehiculo_form = VehiculoForm(self.request.POST)

        if cliente_form.is_valid() and vehiculo_form.is_valid():
            # Guardar Cliente y Vehiculo
            cliente = cliente_form.save()
            vehiculo = vehiculo_form.save(commit=False)
            vehiculo.cliente = cliente
            vehiculo.save()

            # Asignar relacion a AltaVehiculo
            alta_vehiculo.cliente = cliente
            alta_vehiculo.vehiculo = vehiculo
            alta_vehiculo.save()

            return redirect(self.get_success_url())

        # Si alguno de los formularios no es válido, renderizar el formulario nuevamente
        return self.form_invalid(form)
    
class AltaVehiculoDetail(DetailView):
    model = AltaVehiculo