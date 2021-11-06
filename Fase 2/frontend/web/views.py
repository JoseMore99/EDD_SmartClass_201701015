from django.shortcuts import render, redirect
from django.contrib import messages
import requests 
import json

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
        try:
            titulos = request.POST["titulo"]
            contenido = request.POST["Contenido"]
            apunte ={
                "titulos":titulos,
                "contenido":contenido,
                "carnet":Actual["Carnet"]
            }
            requests.post("http://localhost:3000//apuntes",json=apunte)
            messages.success(request, 'Apunte enviado con éxito.')
        except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el Apunte.')
    return render(request,"usuarios.html",context=Actual)

def lst_apuntes(request):
    global Actual
    apun= {
            "carnet": Actual["Carnet"]
        }
    estudiante=requests.get('http://localhost:3000//apuntes',json=apun)
    encontrado= estudiante.json()
    apuntes = []
    for i in encontrado:
        contenido=[]
        contenido.append(i)
        contenido.append(encontrado[i])
        apuntes.append(contenido)
    ctx={
        "apuntes":apuntes,
        "Nombre":Actual['Nombre']
    }
    return render(request,"lst_apuntes.html",context=ctx)

def carga_estu(request):
    JsonEstu = request.FILES["CargaEstu"].read()
    envio = json.loads(JsonEstu.decode('utf-8'))
    requests.post("http://localhost:3000//carga",json=envio)
    try:
        messages.success(request, 'Carga de estudiantes realizado con éxito.')
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar al subir los estudiantes')
    return render(request,"adminis.html")

def carga_apun(request):
    JsonEstu = request.FILES["CargaApun"].read()
    envio = json.loads(JsonEstu.decode('utf-8'))
    requests.post("http://localhost:3000//apuntesM",json=envio)
    try:
        messages.success(request, 'Carga de Apuntes realizado con éxito.')
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el Apunte.')
    return render(request,"adminis.html")

def carga_cursos(request):
    JsonEstu = request.FILES["CargaCursos"].read()
    envio = json.loads(JsonEstu.decode('utf-8'))
    requests.post("http://localhost:3000//cursosEstudiante",json=envio)
    try:
        messages.success(request, 'Carga de cursos realizado con éxito.')
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar los cursos.')
    return render(request,"adminis.html")

def carga_pensum(request):
    JsonEstu = request.FILES["CargaPensum"].read()
    envio = json.loads(JsonEstu.decode('utf-8'))
    requests.post("http://localhost:3000//cursosPensum",json=envio)
    try:
        messages.success(request, 'Carga de cursos realizado con éxito.')
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar los cursos.')
    return render(request,"adminis.html")

def carga_hash(request):
    envio ={
        "tipo":5
    }
    requests.get("http://localhost:3000//reporte",json=envio)
    try:
        messages.success(request, 'Reporte de Apuntes realizado con éxito.')
        ctx ={
            "num":"1"
        }
        return render(request,"reportes.html",ctx)
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el reporte.')
    return render(request,"adminis.html")

def carga_grafo(request):
    envio ={
        "tipo":6
    }
    requests.get("http://localhost:3000//reporte",json=envio)
    try:
        messages.success(request, 'Reporte de Cursos realizado con éxito.')
        ctx ={
            "num":"2"
            }
        return render(request,"reportes.html",ctx)
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el reporte.')
    return render(request,"adminis.html")

def reporte_grafo(request):
    envio ={
        "tipo":7,
        "codigo":request.POST["codigo"]
    }
    requests.get("http://localhost:3000//reporte",json=envio)
    try:
        messages.success(request, 'Reporte de Cursos realizado con éxito.')
        ctx ={
            "num":"3"
            }
        return render(request,"reportes.html",ctx)
    except Exception as e:
            messages.error(request, 'Ocurrió un error al enviar el reporte.')
    return render(request,"adminis.html")

def volverA(request):
    return render(request,"adminis.html")

def Registrarbtn(request):
    return render(request,"registro.html")

def Registro(request):
    carnet = request.POST["car"]
    passw = request.POST["pass"]
    return redirect("inicio")