from flask import Flask, request
from flask_cors import CORS

app= Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})



@app.route("/")
def hola():
    return "Pagina principal"

@app.route("/puerto", methods=['GET'])
def chetget():
    
    return ''

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
    app.run()