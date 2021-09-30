class hoja:
    def __init__(self, orden, EsHoja):
        self.contador = 0 # CONTADOR DE NUMERO DE CLAVES QUE SE POSEE
        self.orden = orden #NUMERO DE RAMAS
        self.padre = None
        self.valores=[]
        self.hijos=[]
        self.EsHoja = EsHoja
    
    def agregar_Valor(self,dato):#AGRENAMOS CLAVES
        if len(self.valores)==0:
            self.valores.append(dato)
        else:
            print(self.valores)
            if dato < self.valores[0]: 
                self.valores.insert(0,dato)
            else:
                i = self.buscarPos(dato)
                self.valores.insert(i+1,dato)

    def agregar_hijo(self,hijo,dato):#AGREGAMOS HIJOS SEGUN LA POCISION DE LA CLAVE
        if len(self.hijos)==0:
            self.hijos.append(hijo)
        else:
            if dato < self.valores[0]: 
                self.hijos.insert(0,hijo)
            else:
                i = self.buscarPos(dato)
                self.hijos.insert(i,hijo)

    def buscarPos(self,dato):#BUSCAR POCISION DEL VALOR A INSERTAR (O DE LA RAMA HIJO)
        i = 0
        while dato > self.valores[i]:
            if(i == len(self.valores)-1):
                return i
                #break
            i+=1
        return i-1

    def buscarHijo(self, dato):
        if len(self.hijos)!=0:
            if dato < self.valores[0]:
                return 0
            else:
                i = self.buscarPos(dato)
                return i
        return -1

    def pagina_llena(self):
        return len(self.valores) == self.orden 

    def min_valores(self):
        return len(self.valores) > self.orden /2
        
class ArbolB:
    def __init__(self,orden):
        self.orden = orden
        self.raiz = None

    def insertar(self, dato):
        self.raiz = self.insertar_nodo(dato, self.raiz)

    def insertar_nodo(self, dato, root):
        if root == None:
            root = hoja(self.orden, True)
            root.agregar_Valor(dato)
        else:
            if root.EsHoja:
                root.agregar_Valor(dato)
            else:
                i = root.buscarHijo(dato)
                root.hijos[i]=self.insertar_nodo(dato,root.hijos[i])
            if root.pagina_llena():
                root = self.separar(root)
        return root

    def separar(self,root):
        print(root.valores)
        #CREAR HERMANO
        Nodo = hoja(self.orden,False)
        if root.EsHoja:
            Nodo.EsHoja=True
        
        #VALOR NUEVO DE PADRE
        m = root.valores[int(len(root.valores)/2):int(len(root.valores)/2)+1]
        #HOJA DE LA DERECHA
        Nodo.valores= root.valores[int(len(root.valores)/2)+1:len(root.valores)]
        Nodo.hijos =  root.hijos[int(len(root.hijos)/2):len(root.hijos)]
        #ACTUALIZAR PADRE
        
        for n in Nodo.hijos:
            n.padre= Nodo# revisar mas adelante!!!!!

        #HOJA DE LA IZQUIERDA
        root.valores= root.valores[0:int(len(root.valores)/2)]
        root.hijos =  root.hijos[0:int(len(root.hijos)/2)]

        if root.padre == None:
            #SI LA RAIZ NO TIENE PADRE SE CREA
            dad =  hoja(self.orden,False)
            dad.agregar_Valor(m[0])
            dad.agregar_hijo(root,root.valores[len(root.valores)-1])
            dad.agregar_hijo(Nodo,Nodo.valores[len(root.valores)-1])

            Nodo.padre= dad
            root.padre = Nodo.padre
            return dad
        else:
            #SI TIENE PADRE 
            root.padre.agregar_Valor(m[0])
            Nodo.padre=root.padre
            root.padre.agregar_hijo(Nodo,Nodo.valores[len(Nodo.valores)-1])
        
        return root
    #PRUEBAS
    def imprimir(self):
        if self.raiz is not None:
            self.imprimir_Nodo(self.raiz)

    def imprimir_Nodo(self, raiz):
        if raiz is not None:
            print()
            if raiz.padre is not None:
                print("Padre", end=":")
                print(raiz.padre.valores)
            print(raiz.valores)
            for i in raiz.hijos:
                self.imprimir_Nodo(i)

tree = ArbolB(5)
tree.insertar(5)
tree.insertar(1)
tree.insertar(7)
tree.insertar(11)
tree.insertar(4)
tree.insertar(17)
tree.insertar(8)
tree.insertar(10)
tree.insertar(23)
tree.insertar(14)
tree.insertar(2)
#tree.imprimir()