from django import forms

from . import models


class altaVehiculoForm(forms.ModelForm):
    class Meta:
        model = models.AltaVehiculo
        fields = "__all__"
