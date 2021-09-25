import Almacen.Matriz_D
import Almacen.ListaDoble
import Almacen.ArbolB
import os

class estudiante:
    def __init__(self,carnet="",creditos="",dpi="",edad="",nombre="",carrera="",correo="",passw=""):
        self.carnet = carnet
        self.creditos = creditos
        self.dpi = dpi
        self.edad = edad
        self.nombre = nombre
        self.carrera = carrera
        self.correo = correo
        self.passw = passw
        self.anios = Almacen.ListaDoble.lista_dob()
    
    def insertar_anio(self, annio):
        apunta = self.anios.head
        while apunta:
            if apunta.contenido.annio == annio:
                return
            apunta = apunta.siguiente
        amio = anios(annio)
        self.anios.insertar(amio)
        
    def insertar_tarea(self, tarea, annio, mes,dia,hora):
        self.insertar_anio(annio)
        apunanio= self.anios.head
        while apunanio:
            if apunanio.contenido.annio==annio:
                break
            apunanio = apunanio.siguiente
        apunanio.contenido.insertar_mes(mes)
        apunmes = apunanio.contenido.meses.head
        while apunmes:
            if apunmes.contenido.mes==mes:
                break
            apunmes = apunmes.siguiente
        apunmes.contenido.MatDis.insertar_elemento(hora,dia,tarea)

    def graftarea(self,annio,mes):
        apunta = self.anios.head

        while apunta:
            if int(apunta.contenido.annio) == int(annio):
                print("entro")
                apunta.contenido.grafmes(mes)
            apunta = apunta.siguiente

    def __str__(self):
        print("Carnet: "+self.carnet)
        print("Creditos: "+self.creditos)
        print("Dpi: "+self.dpi)
        print("Edad: "+self.edad)
        print("Nombre: "+self.nombre)
        print("Carrera: "+self.carrera)
        print("Password: "+self.passw)
        return "-------------------"

class anios:
    def __init__(self, annio):
        self.annio = annio
        self.meses= Almacen.ListaDoble.lista_dob()
        self.semestre = Almacen.ListaDoble.lista_dob()
    
    def insertar_mes(self,mes):
        apunta = self.meses.head
        while apunta:
            if apunta.contenido.mes == mes:
                return
            apunta = apunta.siguiente
        mesi = meses(mes)
        self.meses.insertar(mesi)
    
    def grafmes(self,mes):
        apunta = self.meses.head
        while apunta:
            if apunta.contenido.mes == mes:
                apunta.contenido.graficar_tarea()
            apunta = apunta.siguiente

class meses: 
    def __init__(self, mes):
        self.mes = mes
        self.MatDis = Almacen.Matriz_D.Matriz()
    
    def graficar_tarea(self):
        Archi = open("Matriz.dot","w")
        Archi.write('digraph grid {')
        Archi.write('layout=dot\nlabelloc = "t"')
        Archi.write('edge [weight=1000 style=dashed color=dimgrey]\n')
        temp = self.MatDis.root
        while temp is not None:
            col = temp
            while col is not None:
                try:
                    Archi.write('{}[label="{}" fillcolor=dodgerblue style="filled"]\n'.format(str(hash(col)),col.dato.materi))
                except:
                    valorxy= str(col.x)+","+str(col.y)
                    if valorxy=="-1,-1":
                        Archi.write('{}[label="{}" fillcolor=brown1 style="filled"]\n'.format(str(hash(col)),"Root"))
                    else:
                        Archi.write('{}[label="{}" fillcolor=darkorchid1 style="filled"]\n'.format(str(hash(col)),valorxy))
                col = col.abajo
            temp = temp.siguiente

        temp = self.MatDis.root
        while temp is not None:
            col = temp
            while col.abajo is not None:
                Archi.write('{}->'.format(str(hash(col))))
                col = col.abajo
            Archi.write(str(hash(col))+' [arrowhead=vee, arrowtail=vee, dir=both]\n')
            temp = temp.siguiente
        temp = self.MatDis.root
        while temp is not None:
            col = temp
            Archi.write("rank = same{"+str(hash(col))+'->')
            bul = True
            while col.siguiente is not None:
                Archi.write('{}->'.format(str(hash(col))))
                col = col.siguiente
            Archi.write(str(hash(col))+' [arrowhead=vee, arrowtail=vee, dir=both]}\n')
            temp = temp.abajo
        Archi.write('}')
        Archi.close()
        os.system('dot -Tpng Matriz.dot -o MatrizG.png')

class semestre:
    def __init__(self, numero) -> None:
        self.numero = numero
        self.abb = Almacen.ArbolB.ArbolB()

class tarea:
    def __init__(self,carnet="",nombre="",desc="",materi="",fecha="",hora="",estado=""):
        self.carnet = carnet
        self.nombre = nombre
        self.desc = desc
        self.materi = materi
        self.fecha = fecha
        self.hora = hora
        self.estado = estado
    
    def __str__(self):
        print("Carnet: " + self.carnet)
        print("Nombre: " + self.nombre)
        print("Descripcion: "+ self.desc)
        print("Materia: "+ self.materi)
        print("Fecha: "+ self.fecha)
        print("Hora: "+ self.hora)
        print("Estado: " + self.estado)
        return "-------------------"

class curso:
    def __init__(self, nombre, codigo, creditos, obligatorio,prerrequisito) -> None:
        self.nombre = nombre
        self.codigo = codigo
        self.creditos = creditos
        self.obligatorio = obligatorio
        self.prerrequisito = prerrequisito