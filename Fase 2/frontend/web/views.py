from django.shortcuts import render, redirect
import requests 

# Create your views here.

def inicio (request):

    return render(request,"login.html")

def adminis(request):
    if request.method == "POST":
        usuario = request.POST["usu"]
        contrasenia = request.POST["contra"]
        if usuario == "admin" and contrasenia == "admin":
            return render(request,"adminis.html")
        usu = {
            "carnet": usuario
        }
        estudiante=requests.get('http://localhost:3000//estudiante',json=usu)
        encontrado= estudiante.json()
        if contrasenia == encontrado["password"]:
            return render(request,"usuarios.html",context=encontrado) 
        
    return redirect("inicio")