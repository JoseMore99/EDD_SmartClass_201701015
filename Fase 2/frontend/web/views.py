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
        
        estudiante=requests.get('http://127.0.0.1:5000/chet',usuario)
        
    return redirect("inicio")