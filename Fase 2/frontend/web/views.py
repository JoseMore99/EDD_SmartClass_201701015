from django.shortcuts import render, redirect
import requests 

# Create your views here.
Actual ={}
def inicio (request):

    return render(request,"login.html")

def adminis(request):
    global Actual
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
        Actual = encontrado
        if contrasenia == encontrado["password"]:
            return render(request,"usuarios.html",context=encontrado) 
        
    return redirect("inicio")

def usuApunte(request):
    global Actual
    return render(request,"apuntes.html",Actual)

def apunte(request):
    global Actual
    if request.method == "POST":
        titulos = request.POST["titulo"]
        contenido = request.POST["Contenido"]
        apunte ={
            "titulos":titulos,
            "contenido":contenido,
            "carnet":Actual["Carnet"]
        }
        requests.post("http://localhost:3000//apuntes",json=apunte)
    return render(request,"usuarios.html",context=Actual) 