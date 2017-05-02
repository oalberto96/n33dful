from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.models import User
from main.models import Usuario, Escuela, Sexo
from django.utils import timezone


def home(request):
    return render(request, "main/login_home.html")

def iniciar_sesion(request):
    return render(request, "main/login.html")

def crear_cuenta(request):
    return render(request, "main/signup.html")

def registrar(request):
    #user
    username = request.POST['username']
    password = request.POST['password']
    #Usuairo
    email = request.POST['correo']
    #sexo = request.POST['sexo']
    #escuela = request.POST['escuela']
    nombre = request.POST['nombre']
    apellido = request.POST['apellido']
    fecha_nacimiento = request.POST['nacimiento']
    sexo = Sexo.objects.get(nombre_sexo="Mujer")
    escuela = Escuela.objects.get(nombre="Territorio Sur")
    user = User.objects.create_user(username=username,password=password)
    user.save()
    usuario = Usuario(id_escuela=escuela,id_sexo=sexo,nombre=nombre,apellido=apellido,fecha_nacimiento=fecha_nacimiento,correo=email,id_user=user)
    usuario.save()

    return home(request)

def solicitud_login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request,username=username,password=password)
    if user is not None:
        login(request, user)
        return home(request)
    else:
        return home(request)

def salir(request):
    logout(request)
    return home(request)
