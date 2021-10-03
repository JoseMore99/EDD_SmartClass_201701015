from Lex import tokens
from objetos import estudiante, tarea,anios
from Almacen.AVL import avl
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
            #print(i)
            pass
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
        estuAdd.carnet = estuAdd.carnet.replace('"','')
        estuAdd.carrera = estuAdd.carrera.replace('"','')
        estuAdd.correo = estuAdd.correo.replace('"','')
        estuAdd.nombre = estuAdd.nombre.replace('"','')
        estuAdd.dpi = estuAdd.dpi.replace('"','')
        try:
            estuAdd.edad = estuAdd.edad.replace('"','')
            estuAdd.creditos = estuAdd.creditos.replace('"','')
        except:
            pass
        estuAdd.passw = estuAdd.passw.replace('"','')
        Nuevo = estudiante(estuAdd.carnet,estuAdd.creditos,estuAdd.dpi,estuAdd.edad,estuAdd.nombre,estuAdd.carrera,estuAdd.correo,estuAdd.passw)
        LestuYtare.append(Nuevo)
        avl.insertar(int(estuAdd.carnet),Nuevo)
    if boolTarea:
        tareADD.carnet = tareADD.carnet.replace('"','')
        tareADD.nombre = tareADD.nombre.replace('"','')
        tareADD.desc = tareADD.desc.replace('"','')
        tareADD.materi = tareADD.materi.replace('"','')
        tareADD.fecha = tareADD.fecha.replace('"','')
        tareADD.hora = tareADD.hora.replace('"','')
        splitHora = tareADD.hora.split(':')
        tareADD.estado = tareADD.estado.replace('"','')
        Nuevo = tarea(tareADD.carnet,tareADD.nombre,tareADD.desc,tareADD.materi,tareADD.fecha,tareADD.hora,tareADD.estado)
        datos = tareADD.fecha.split("/")
        Mes=int(datos[1])
        anio=int(datos[2])
        dia=int(datos[0])
        carne = int(tareADD.carnet)
        apunta = avl.buscador(carne)
        print(apunta.estu.carnet)
        apunta.estu.insertar_tarea(Nuevo, anio, Mes,dia,int(splitHora[0]))
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
        if Tipo =="DPI":
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
        if Tipo =="Correo":
            estuAdd.correo=t[1]
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
                | TCORREO
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