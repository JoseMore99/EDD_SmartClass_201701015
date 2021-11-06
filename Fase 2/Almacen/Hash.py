from Almacen.ListaDoble import lista_dob

class apunte:
    def __init__(self, titulo, contenido):
        self.titulo= titulo
        self.contenido = contenido
        
class NodoHash:
    def __init__(self,carnet):
        self.siguiente = None
        self.carnet = carnet
        self. apuntes = lista_dob()#guardara titulo y contenido de todos los apuntes del estudiante

class THash:
    def __init__(self, tamanio):
        self.tamanio = tamanio
        self.tabla = [NodoHash for x in range(tamanio)]
        self.cantidad =0

        for i in range(tamanio):
            self.tabla[i] = None

    def insertar(self,llave,titulo,contenido):
        pocision = self.formulaHash(llave)
        apunteNew = apunte(titulo,contenido)
        if self.tabla[pocision] is None:
            self.tabla[pocision] = NodoHash(llave)
            self.tabla[pocision].apuntes.insertar(apunteNew)
            self.cantidad+=1
        elif self.tabla[pocision].carnet == llave:
            self.tabla[pocision].apuntes.insertar(apunteNew)
        else:
            contador = 1
            pocision = self.formulaHash(pocision+contador)
            while self.tabla[pocision] is not None:
                pocision = self.formulaHash(pocision+contador)
                contador+=1
            self.tabla[pocision] = NodoHash(llave)
            self.cantidad+=1
            self.tabla[pocision].apuntes.insertar(apunteNew)
        if self.cantidad> (self.tamanio/2):
            self.rehash()

    def formulaHash(self, llave):
        pocision  = llave%self.tamanio
        return pocision

    def devolver(self, llave):
        apuntes=[]
        for i in self.tabla:
            if i is None:
                continue
            if i.carnet == llave:
                apuntador = i.apuntes.head
                while apuntador:
                    apuntes.append(apuntador.contenido)
                    apuntador = apuntador.siguiente
        return apuntes
    
    def rehash(self):
        num = self.tamanio +1
        print(self.tamanio)
        bol= True
        while bol:
            for i in range(2,num):
                if num % i == 0:
                    break
                elif i == num-1:
                    self.tamanio=num
                    while True:
                        self.tabla.append(None)
                        if len(self.tabla)==self.tamanio:
                            break
                    bol=False
            num +=1

prueba = THash(17)
prueba.insertar(14,"","")
prueba.insertar(31,"","")
prueba.insertar(62,"","")
prueba.insertar(26,"","")
prueba.insertar(39,"","")
prueba.insertar(44,"","")
prueba.insertar(45,"","")
prueba.insertar(22,"","")
prueba.insertar(15,"","")
prueba.insertar(16,"","")

for i in range(len(prueba.tabla)):
    if prueba.tabla[i] is None:
       # print(str(i)+"- None")
        continue
   #print(str(i)+"-"+str(prueba.tabla[i].carnet))