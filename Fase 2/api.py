from flask import Flask, request,jsonify
from flask_cors import CORS
from Sintac import parser
import generador 
import os
from Almacen.AVL import avl

app= Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route("/")
def hola():
    return "Pagina principal"

#CARGA MASIMA DE ESTUDIANTES CURSO,Y TAREAS
@app.route("/carga", methods=['POST'])
def cargaMasivaEstu():
    peticion = request.json
    if peticion['tipo']=="estudiante":
        f = open(peticion['path'], "r", encoding="utf-8")
        mensaje = f.read()
        f.close()
        parser.parse(mensaje)
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
        os.system('dot -Tsvg grafAVL.dot -o ArbolAVL1.svg')
        return 'GRAFICA AVL REALIZADA CON EXITO!!'
    elif peticion['tipo']==1:
        print(peticion['carnet'])
        print(peticion['año'])
        print(peticion['mes'])
        puntero = avl.buscador(peticion['carnet'])
        puntero.estu.graftarea(peticion['año'],peticion['mes'])
        return 'GRAFICA MATRIZ DE TAREAS REALIZADA CON EXITO!!'
    return ''

@app.route("/estudiante", methods=['POST'])
def estudiantesPost():
    
    return ''
    
@app.route("/estudiante", methods=['PUT'])
def estudiantesPut():
    
    return ''

@app.route("/estudiante", methods=['DELETE'])
def estudiantesDelete():
    
    return ''

@app.route("/estudiante", methods=['GET'])
def estudiantesGet():
    
    return ''

@app.route("/recordatorio", methods=['POST'])
def recordatorioPost():
    
    return ''

@app.route("/recordatorio", methods=['PUT'])
def recordatorioPut():
    
    return ''

@app.route("/recordatorio", methods=['DELETE'])
def recordatorioDelete():
    
    return ''

@app.route("/recordatorio", methods=['GET'])
def recordatorioGet():
    
    return ''

@app.route("/cursosEstudiante", methods=['POST'])
def cursosEstudiantePost():
    
    return ''

@app.route("/cursosPensum", methods=['POST'])
def cursosPensumPost():
    
    return ''

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