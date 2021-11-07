import copy
import os
class hoja:
    def __init__(self, orden):
        self.contador = 0 # CONTADOR DE NUMERO DE CLAVES QUE SE POSEE
        self.orden = orden #NUMERO DE RAMAS
        self.valores =[0 for x in range(orden)] #CLAVES DE LA HOJA
        self.hijos = [hoja for x in range(orden)]
        #IMPORTANTE INICIALIZAR HIJOS PARA EVITAR ERRORES  
        for i in range(orden):
            self.hijos[i] = None

class Arbol_B:
    def __init__(self, orden):
        self.orden = orden
        self.raiz = hoja(5)
        self.apunta= None
        self.listado=[]

    #BUSCAR CAAMINO A INSERTAR NODO
    def insertar(self,valor):
        self.listado.append(valor.nombre)
        Arriba = False
        Mediana = 0
        Nodonew = None
        Actual = None
        objeto_estatico=[Arriba,Mediana,Nodonew,Actual]
        self.insertar_nodo(self.raiz, valor, objeto_estatico)
        if objeto_estatico[0]:
            objeto_estatico[3] = hoja(self.orden)
            objeto_estatico[3].contador = 1
            objeto_estatico[3].valores[1] = objeto_estatico[1]
            objeto_estatico[3].hijos[0] = self.raiz
            objeto_estatico[3].hijos[1] = objeto_estatico[2]
            self.raiz = objeto_estatico[3]

    def insertar_nodo(self, PunteroHoja, valor, objeto_estatico):
        camino = [0]  
        if PunteroHoja == None:
            objeto_estatico[0]= True 
            objeto_estatico[1] = valor 
            objeto_estatico[2] = None 
        else:
            aux = self.buscarHoja(PunteroHoja, valor, camino)
            if aux:
                objeto_estatico[0] = False
                return
            self.insertar_nodo(PunteroHoja.hijos[camino[0]], valor, objeto_estatico)

            if objeto_estatico[0]:
                if PunteroHoja.contador==(PunteroHoja.orden-1):#VER SI LA HOJA ESTA LLENA
                    self.dividir(PunteroHoja,objeto_estatico[1],copy.deepcopy(objeto_estatico[2]),camino, objeto_estatico)
                else:#SI NO ESTA LLENA AGREGAMOS EL VALOR
                    objeto_estatico[0] = False
                    self.AñadirHoja(PunteroHoja,objeto_estatico[1],objeto_estatico[2],camino[0])

    def buscarHoja(self,puntero, valor, camino):
        encontrado = False
        try:
            if valor.codigo < puntero.valores[1].codigo :
                camino[0] = 0   
                encontrado = False
            else: 
                camino[0] = puntero.contador #REVISAR LUEGO!!!!!!!
                if puntero.valores[camino[0]] is None:
                    camino[0]-=1
                while (valor.codigo < puntero.valores[camino[0]].codigo) and (camino[0] > 1):
                    camino[0] = camino[0] - 1
                encontrado = valor.codigo == puntero.valores[camino[0]].codigo
            return encontrado
        except:
            if valor.codigo < puntero.valores[1] :
                camino[0] = 0   
                encontrado = False
            else: 
                camino[0] = puntero.contador #REVISAR LUEGO!!!!!!!
                if puntero.valores[camino[0]] is None:
                    camino[0]-=1
                while (valor.codigo < puntero.valores[camino[0]]) and (camino[0] > 1):
                    camino[0] = camino[0] - 1
                encontrado = valor.codigo == puntero.valores[camino[0]]
            return encontrado

    def AñadirHoja(self ,PunteroHoja,Mediana,Nodonew,camino):
        i = PunteroHoja.contador
        while i >= camino + 1:
            PunteroHoja.valores[i + 1] = PunteroHoja.valores[i]
            PunteroHoja.hijos[i + 1] = PunteroHoja.hijos[i]
            i = i-1
        PunteroHoja.valores[camino + 1] = Mediana
        PunteroHoja.hijos[camino + 1] = Nodonew
        PunteroHoja.contador = PunteroHoja.contador + 1

    def dividir(self, PunteroHoja, valor, copia, camino, objeto_estatico):
        DerMediana = self.orden / 2 if (camino[0] <= self.orden / 2) else self.orden / 2 + 1
        DerMediana = int(DerMediana)
        objeto_estatico[2] = hoja(5)
        i = DerMediana + 1
        while i < self.orden:
            objeto_estatico[2].valores[i - DerMediana] = PunteroHoja.valores[i]
            objeto_estatico[2].hijos[i - 1] = PunteroHoja.hijos[i]
            i = i + 1
        objeto_estatico[2].contador = (self.orden -1) - DerMediana #ASIGANDO VCUANTOS VALORES SE QUEDAN EN NODONEW
        PunteroHoja.contador = DerMediana
        if camino[0] <= (self.orden / 2): 
            self.AñadirHoja(PunteroHoja,valor, copia, camino[0])
        else:
            self.AñadirHoja(objeto_estatico[2], valor, copia, camino[0] - DerMediana) 
        objeto_estatico[1] = PunteroHoja.valores[PunteroHoja.contador]
        objeto_estatico[2].hijos[0] = PunteroHoja.hijos[PunteroHoja.contador]
        PunteroHoja.contador = PunteroHoja.contador -1
    
    def buscandoB(self,codigo):
        self.buscador(self.raiz,codigo)
        devolver= self.apunta
        self.apunta= None
        return devolver

    def buscador(self, raiz, codigo):
        for i in range(raiz.contador):
            if raiz.valores[i+1].codigo==codigo:
                self.apunta=raiz.valores[i+1]
                return
        for i in raiz.hijos:
            if i == None:
                continue
            self.buscador(i,codigo) 
        

#arbolB = Arbol_B(5)
#arbolB.insertar(1)
#arbolB.insertar(2)
#arbolB.insertar(3)
#arbolB.insertar(4)
#arbolB.insertar(5)
#arbolB.insertar(6)
#arbolB.insertar(7)
#arbolB.insertar(8)



        

#graf(arbolB.raiz)