from django.http import HttpResponse
from django.urls import path
from Aplicacion.views import Inicio, Registro_Cliente, Buscar_Cliente

urlpatterns = [
    path("", Registro_Cliente, name= "registro_cliente"),
    path("Incio", Inicio),
    path("buscar", Buscar_Cliente, name='buscar_cliente'),
    path("registro-exito", lambda request: HttpResponse('Registro exitoso'), name='registro_exito')
]