from flask import Flask, request,jsonify
from flask_cors import CORS
from Sintac import parser
import generador 
import os
from Almacen.AVL import avl
from Almacen.ArbolB2 import Arbol_B
from Almacen.Hash import THash
from objetos import curso,estudiante,tarea

app= Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

Pensum = Arbol_B(5)
Apuntes = THash(7)
@app.route("/")
def hola():
    return "Pagina principal"

#CARGA MASIMA DE ESTUDIANTES CURSO,Y TAREAS
@app.route("/carga", methods=['POST'])
def cargaMasivaEstu():
    peticion = request.json
    """ if peticion['tipo']=="estudiante":
        f = open(peticion['path'], "r", encoding="utf-8")
        mensaje = f.read()
        f.close()
        parser.parse(mensaje)
        return 'Carga Masiva de Estudiantes con exito'
    elif peticion['tipo']=="recordatorio":
        try:
            f = open(peticion['path'], "r", encoding="utf-8")
            mensaje = f.read()
            f.close()
            parser.parse(mensaje)
        except: 
            print("ya cargo")
        return 'Carga Masiva de Tareas con exito' """
    for i in peticion['estudiantes']:
        carnet = i['carnet']
        print(carnet)
        carrera = i['carrera']
        correo = i['correo']
        nombre = i['nombre']
        dpi = i['DPI']
        edad = i['edad']
        creditos = 0#i['creditos']
        passw = i['password']
        Nuevo = estudiante(carnet,creditos,dpi,edad,nombre,carrera,correo,passw)
        avl.insertar(int(carnet),Nuevo)
    return 'Carga Masiva de Estudiantes con exito'

@app.route("/reporte", methods=['GET'])
def reportes():
    peticion = request.json
    if peticion['tipo']==0:
        archi = open("grafAVL.dot","w")
        archi.write("digraph G{\nnode [shape=circle];\n")
        generador.grafAVL(avl.raiz,archi)
        archi.write("\n}")
        archi.close()
        os.system('dot -Tsvg grafAVL.dot -o  frontend/web/static/ArbolAVL1.svg')
        return 'GRAFICA AVL REALIZADA CON EXITO!!'
    elif peticion['tipo']==1:
        puntero = avl.buscador(int(peticion['carnet']))
        print(puntero.estu.carnet)
        puntero.estu.graftarea(peticion['año'],peticion['mes'])
        return 'GRAFICA MATRIZ DE TAREAS REALIZADA CON EXITO!!'
    elif peticion['tipo']==3:
        generador.grafB(Pensum.raiz)
        return 'GRAFICA ARBOL B DE PENSUM REALIZADA CON EXITO!!'
    elif peticion['tipo']==4:
        carne = peticion["carnet"]
        annio = peticion["año"]
        semestre = peticion["semestre"]
        apunta = avl.buscador(carne)
        apuntaAnio= apunta.estu.devolv_anio(annio)
        if semestre == '"1"'or semestre == '"2"':
            semestre = semestre.replace('"','')
        if int(semestre) ==1:
            generador.grafB(apuntaAnio.semestre.head.contenido.abb.raiz)
        elif int(semestre) ==2:
            generador.grafB(apuntaAnio.semestre.head.siguiente.contenido.abb.raiz)
    elif peticion['tipo']==5:
        archi = open("grafAVL.dot","w")
        archi.write("digraph G{\nnode [shape=square];\n")
        for i in Apuntes.tabla:
            if i == None:
                continue
            archi.write("rank = same{"+str(i.carnet)+"->")
            apuntes = Apuntes.devolver(i.carnet)
            cuenta=0 
            for j in apuntes:
                cuenta+=1
                if cuenta == len(apuntes):
                    archi.write(j.titulo)
                    continue
                archi.write('"'+j.titulo+'"->')
            archi.write("}\n")
            cuenta=0 
        for i in Apuntes.tabla:
            cuenta+=1
            if i == None:
                if cuenta == len(apuntes):
                    archi.write('" "')
                    continue
                archi.write('" "->')
                continue
            if cuenta == len(apuntes):
                    archi.write(str(i.carnet))
                    continue
            archi.write(str(i.carnet)+"->")
        archi.write("\n}")
        archi.close()
        os.system('dot -Tsvg grafAVL.dot -o  frontend/web/static/hash.svg')
        
        return 'GRAFICA Tabla hash DE apuntes REALIZADA CON EXITO!!'
    return ''

@app.route("/estudiante", methods=['POST'])
def estudiantesPost():
    peticio = request.json
    carnet = peticio['carnet']
    carrera = peticio['carrera']
    correo = peticio['correo']
    nombre = peticio['nombre']
    dpi = peticio['DPI']
    edad = peticio['edad']
    creditos = peticio['creditos']
    passw = peticio['password']
    Nuevo = estudiante(carnet,creditos,dpi,edad,nombre,carrera,correo,passw)
    avl.insertar(int(carnet),Nuevo)
    return 'ESTUDIANTE INGRESADO!'
    
@app.route("/estudiante", methods=['PUT'])
def estudiantesPut():
    peticio = request.json
    carnet = peticio['carnet']
    carrera = peticio['carrera']
    correo = peticio['correo']
    nombre = peticio['nombre']
    dpi = peticio['DPI']
    edad = peticio['edad']
    creditos = peticio['creditos']
    passw = peticio['password']
    Nuevo = estudiante(carnet,creditos,dpi,edad,nombre,carrera,correo,passw)
    avl.eliminar(int(carnet))
    avl.insertar(int(carnet),Nuevo)
    return 'ESTUDIANTE MODIFICADO'

@app.route("/estudiante", methods=['DELETE'])
def estudiantesDelete():
    peticio = request.json
    carnet = peticio['carnet']
    avl.eliminar(int(carnet))
    return 'ESTUDIANTE ELIMINADO'

@app.route("/estudiante", methods=['GET'])
def estudiantesGet():
    i = request.json
    carnet = i["carnet"]
    apunta = avl.buscador(int(carnet))
    print(apunta.estu.carnet)
    datos ={
        'Carnet': apunta.estu.carnet,
        'Nombre': apunta.estu.nombre,
        'Creditos': apunta.estu.creditos,
        'DPI': apunta.estu.dpi,
        'edad': apunta.estu.edad,
        'Correo': apunta.estu.correo,
        'password':  apunta.estu.passw,
    }
    return datos

@app.route("/recordatorio", methods=['POST'])
def recordatorioPost():
    peticio = request.json
    carnet = peticio['Carnet']
    nombre = peticio['Nombre']
    desc = peticio['Descripcion']
    materi = peticio['Materia']
    fecha = peticio['Fecha']
    hora = peticio['Hora']
    splitHora = hora.split(':')
    estado = peticio['Estado']
    Nuevo = tarea(carnet,nombre,desc,materi,fecha,hora,estado)
    datos = fecha.split("/")
    Mes=int(datos[1])
    anio=int(datos[2])
    dia=int(datos[0])
    carne = int(carnet)
    apunta = avl.buscador(carne)
    print(apunta.estu.carnet)
    apunta.estu.insertar_tarea(Nuevo, anio, Mes,dia,int(splitHora[0]))
    return 'RECORDATORIO AÑADIDO!'

@app.route("/recordatorio", methods=['PUT'])
def recordatorioPut():
    return ''
@app.route("/recordatorio", methods=['DELETE'])
def recordatorioDelete():  
    return ''

@app.route("/recordatorio", methods=['GET'])
def recordatorioGet():
    peticio = request.json
    carnet = peticio['Carnet']
    fecha = peticio['Fecha']
    hora = peticio['Hora']
    splitHora = hora.split(':')
    datos = fecha.split("/")
    Mes=int(datos[1])
    anio=int(datos[2])
    dia=int(datos[0])
    apunta = avl.buscador(int(carnet))
    apunta2= apunta.estu.devolv_anio(anio)
    apunta3 = apunta2.devolv_mes(Mes)
    encontrado= apunta3.MatDis.buscar_dato(int(splitHora[0]),dia)
    datos ={
        "Carnet": encontrado.carnet,
        "Nombre": encontrado.nombre,
        "Descripcion":encontrado.desc,
        "Materia": encontrado.materi,
        "Fecha": encontrado.fecha,
        "Hora": encontrado.hora,
        "Estado": encontrado.estado
    }
    return datos

@app.route("/cursosEstudiante", methods=['POST'])
def cursosEstudiantePost():
    peticion=request.json
    for i in peticion["Estudiantes"]:
        carnet = i["Carnet"]
        apunta = avl.buscador(carnet)
        for j in i["Años"] :
            annio = j["Año"]
            for k in j["Semestres"]:
                semestre = k["Semestre"]
                for l in k['Cursos']:
                    codigo = int(l["Codigo"])
                    nombre = l["Nombre"]
                    creditos=l["Creditos"]
                    prerre=l["Prerequisitos"]
                    obliga=l["Obligatorio"]
                    nuevo  = curso(nombre,codigo,creditos,obliga,prerre)
                    apunta.estu.insertarCurso(nuevo,semestre, annio)
                    
    return 'Cargra de cursos de estudiantes exitosa'

@app.route("/cursosPensum", methods=['POST'])
def cursosPensumPost():
    peticion = request.json
    for i in peticion['Cursos']:
        codigo = int(i["Codigo"])
        nombre = i["Nombre"]
        creditos=i["Creditos"]
        prerre=i["Prerequisitos"]
        obliga=i["Obligatorio"]
        nuevo  = curso(nombre,codigo,creditos,obliga,prerre)
        Pensum.insertar(nuevo)
        #Pensum.insertar(int(i["Codigo"]))
    return 'Carga de cursos en Pensum completa'

@app.route("/apuntes", methods=['POST'])
def apuntesPost():
    peticion = request.json
    titulos = peticion["titulos"]
    contenido = peticion["contenido"]
    Carnet=int(peticion["carnet"])
    Apuntes.insertar(Carnet,titulos,contenido)
    return 'Carga de apunte completa'

@app.route("/apuntes", methods=['GET'])
def apuntesGet():
    lista ={}
    peticion = request.json
    Carnet=int(peticion["carnet"])
    apuntes = Apuntes.devolver(Carnet)
    for i in apuntes:
        lista[i.titulo]=i.contenido
    return lista
    
@app.route("/apuntesM", methods=['POST'])
def apuntesMasiva():
    peticion = request.json
    for i in peticion['usuarios']:
        carnet = i['carnet']
        print(carnet)
        for j in i['apuntes']:
            titulos = j["Título"]
            contenido = j["Contenido"]
            Apuntes.insertar(carnet,titulos,contenido)
        
    return 'Carga masiva de apuntes competa'



#URLS DE PRUEBAS UNICAMENTE 
@app.route("/pagina2")
def pagina2():
    return "Hola :)"

@app.route("/pagina3", methods=['POST'])
def pagina3():
    nombre = request.form.get('nombre')
    return "HOLA "+str(nombre)

if __name__=="__main__":
    app.run(debug=True,port=3000)