from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = 'altaVehiculo'

urlpatterns = [
    path("", TemplateView.as_view(template_name="altaVehiculo/index.html"), name="home"),
    path('nuevo_alta_vehiculo',views.AltaVehiculoCreate.as_view(), name='create'),
    path('detalle_alta_vehiculo/<int:pk>/', views.AltaVehiculoDetail.as_view(), name='detalle_alta_vehiculo'),
]
