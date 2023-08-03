from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import AltaVehiculo, Cliente, Vehiculo
from .forms import altaVehiculoForm
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
    FormView
)



class AltaVehiculoCreate(FormView):
    form_class = altaVehiculoForm
    template_name = 'altaVehiculo/alta_vehiculo_form.html'
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        # Crear instancia de Cliente
        cliente = Cliente.objects.create(
            nombre=form.cleaned_data['cliente_nombre'],
            apellido=form.cleaned_data['cliente_apellido'],
            dni=form.cleaned_data['cliente_dni'],
            telefono=form.cleaned_data['cliente_telefono'],
            domicilio=form.cleaned_data['cliente_domicilio']
        )

        # Crear instancia de Vehiculo
        vehiculo = Vehiculo.objects.create(
            marca=form.cleaned_data['vehiculo_marca'],
            modelo=form.cleaned_data['vehiculo_modelo'],
            año=form.cleaned_data['vehiculo_año'],
            patente=form.cleaned_data['vehiculo_patente'],
            km=form.cleaned_data['vehiculo_km']
        )

        # Crear instancia de AltaVehiculo con las relaciones a Cliente y Vehiculo
        alta_vehiculo = AltaVehiculo.objects.create(
            cliente_id=cliente,
            vehiculo_id=vehiculo,
            # Asignar otros campos de AltaVehiculo aquí
        )

        return redirect(self.success_url)
class AltaVehiculoDetail(DetailView):
    model = AltaVehiculo