from flask import Flask, request,jsonify
from flask_cors import CORS
from Sintac import parser

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

@app.route("/puerto", methods=['POST'])
def chetPost():
    
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