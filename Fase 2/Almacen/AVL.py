class NodoA:
    def __init__(self, id, estu):
        self.id = id
        self.estu = estu
        self.izq = None
        self.der = None

class AVL:
    def __init__(self):
        self.raiz = None
        self.altura = -1
        self.equi = 0
        self.apunta =None

    def insertar(self,id,estu):
        nuevo = NodoA(id,estu)
        if self.raiz == None:
            self.raiz = nuevo
            self.raiz.izq = AVL()
            self.raiz.der = AVL()
        elif id > self.raiz.id:
            self.raiz.der.insertar(id,estu)
        elif id < self.raiz.id:
            self.raiz.izq.insertar(id,estu)
        else: 
            print("El estudiante ya existe!! :o")
        self.equilibrar()

    def eliminar(self, id):
        self.raiz=self.delete(self.raiz,id)
        print("se elimino "+str(id))

    def delete(self, raiz,id):
        if id < raiz.id:
            raiz.izq.raiz = self.delete(raiz.izq.raiz, id)
        elif id > raiz.id:
            raiz.der.raiz = self.delete(raiz.der.raiz, id)
        elif id == raiz.id:
            if raiz.der.raiz==None and raiz.izq.raiz==None:#NO TIENE HIJOS
                return None
            elif raiz.der.raiz and raiz.izq.raiz==None:#TIENE UN HIJO A LA DERECHA
                raiz = raiz.der.raiz
            elif raiz.izq.raiz and raiz.der.raiz==None:#TIENE UN HIJO A LA IZQUIERDA
                raiz = raiz.izq.raiz
            else:#TIENE DOS HIJOS 
                temp =  self.MaxIz(raiz.izq.raiz)
                raiz = self.delete(raiz,temp.id)
                raiz.id = temp.id
                raiz.estu = temp.estu
        self.equilibrar()
        return raiz
                

    
    def MaxIz(self,raiz):
        while(raiz.der.raiz):
            raiz=raiz.der.raiz
        return raiz
    
    def equilibrar(self):
        self.actuAltura(recursivo= False)
        self.actuEquili(False)
        while self.equi < -1 or self.equi > 1:
            if self.equi > 1:
                if self.raiz.izq.equi < 0:
                    self.raiz.izq.RotIz()
                    self.actuAltura()
                    self.actuEquili()
                self.RorDerecha()
                self.actuAltura()
                self.actuEquili()
            if self.equi < -1:
                if self.raiz.der.equi > 0:
                    self.raiz.der.RorDerecha()
                    self.actuAltura()
                    self.actuEquili()
                self.RotIz()
                self.actuAltura()
                self.actuEquili()


    def actuAltura(self, recursivo =  True):
        if self.raiz == None:
            self.altura = -1
        else:
            if recursivo:
                if self.raiz.izq != None:
                    self.raiz.izq.actuAltura()
                if self.raiz.der != None:
                    self.raiz.der.actuAltura()
            self.altura = max(self.raiz.izq.altura, self.raiz.der.altura) + 1

    def actuEquili(self, recursivo = True):
        if self.raiz == None:
            self.equi = 0
        else:
            if recursivo:
                if self.raiz.izq != None:
                    self.raiz.izq.actuEquili()
                if self.raiz.der != None:
                    self.raiz.der.actuEquili()
            self.equi = self.raiz.izq.altura - self.raiz.der.altura

    def RorDerecha(self):
        raiz = self.raiz
        self.raiz = raiz.izq.raiz
        raiz.izq.raiz = self.raiz.der.raiz
        self.raiz.der.raiz = raiz

    def RotIz(self):
        raiz = self.raiz
        self.raiz = raiz.der.raiz
        raiz.der.raiz = self.raiz.izq.raiz
        self.raiz.izq.raiz = raiz

    def buscador(self, id):
        self.buscar(self.raiz, id)
        return self.apunta
    
    def buscar (self, raiz, id):
        if raiz:
            if raiz.id == id:
                self.apunta = raiz
                return
            self.buscar(raiz.izq.raiz, id)
            self.buscar(raiz.der.raiz, id)

avl = AVL()