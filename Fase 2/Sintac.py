from Lex import tokens
from objetos import estudiante, tarea
# dictionary of names
names = {}

LestuYtare=[]
estuAdd= estudiante()
tareADD = tarea()
boolEstu = False
boolTarea= False

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    for i in LestuYtare:
        try:
            print(i)
        except:
            print("papitas")
            
def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
tipoEl=""
def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'
    global boolTarea
    global boolEstu
    global estuAdd
    if boolEstu:
        Nuevo = estudiante(estuAdd.carnet,estuAdd.creditos,estuAdd.dpi,estuAdd.edad,estuAdd.nombre,estuAdd.carrera,estuAdd.correo,estuAdd.passw)
        LestuYtare.append(Nuevo)
    if boolTarea:
        Nuevo = tarea(tareADD.carnet,tareADD.nombre,tareADD.desc,tareADD.materi,tareADD.fecha,tareADD.hora,tareADD.estado)
        LestuYtare.append(Nuevo)
        
def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    global boolTarea
    global boolEstu
    global tipoEl
    tipoEl = t[3]
    if t[3]=='"user"':
        boolEstu = True
        boolTarea= False
    if t[3]=='"task"':
        boolEstu = False
        boolTarea= True

def p_items(t):
    """items : items item
             | item
    """
    

Tipo=""
def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    if boolEstu:
        if Tipo =="Carnet":
            estuAdd.carnet=t[1]
        if Tipo =="Dpi":
            estuAdd.dpi=t[1]
        if Tipo =="Nombre":
            estuAdd.nombre=t[1]
        if Tipo =="Carrera":
            estuAdd.carrera=t[1]
        if Tipo =="Password":
            estuAdd.passw=t[1]
        if Tipo =="Creditos":
            estuAdd.creditos=t[1]
        if Tipo =="Edad":
            estuAdd.edad=t[1]
    elif boolTarea:
        if Tipo =="Carnet":
            tareADD.carnet=t[1]
        if Tipo =="Nombre":
            tareADD.nombre=t[1]
        if Tipo =="Descripcion":
            tareADD.desc = t[1]
        if Tipo =="Materia":
            tareADD.materi = t[1]
        if Tipo =="Fecha":
            tareADD.fecha = t[1]
        if Tipo =="Hora":
            tareADD.hora = t[1]
        if Tipo =="Estado":
            tareADD.estado = t[1]
def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                """
    global Tipo
    Tipo=t[1]

def p_error(t):
    print("ERROR SINTACTICO '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()