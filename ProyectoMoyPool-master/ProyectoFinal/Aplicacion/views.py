from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import Formulario_Registro_Cliente, Formulario_Busqueda_Cliente
from .models import Registro_Cliente, Cliente

def Inicio(request):
    return render(request,'Lista_Clientes/index.html')

def Registro_Cliente (request):
    if request.method == 'POST':
        form = Formulario_Registro_Cliente(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            email = form.cleaned_data['email']
            guardado = Cliente.objects.create(nombre=nombre, apellido=apellido, email=email)
            Cliente.save(guardado)
            return redirect("buscar_cliente")
            
    else:
        form = Formulario_Registro_Cliente()

    return render(request, 'Lista_Clientes/Registro_Cliente.html', {'form': form})

def Buscar_Cliente(request):
    if request.method == 'POST':
        form = Formulario_Busqueda_Cliente(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            # Buscar el cliente por email
            cliente = Cliente.objects.filter(email=email).first()
            if cliente:
                return render(request, 'Lista_Clientes/Resultado_Busqueda.html', {'cliente': cliente})
            else:
                form.add_error(None, "Cliente no encontrado.")
    else:
        form = Formulario_Busqueda_Cliente()

    return render(request, 'Lista_Clientes/Buscar_Cliente.html', {'form': form})