from Sintac import parser

f = open('Estudiantes.txt', "r", encoding="utf-8")
mensaje = f.read()
f.close()
parser.parse(mensaje)
