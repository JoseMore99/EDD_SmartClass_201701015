class NodoLiD: #Lista doble
    def __init__(self, contenido= None, siguiente= None, anterior= None):
        self.contenido = contenido
        self.siguiente = siguiente
        self.anterior = anterior
    
class lista_dob:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        
    def insertar(self, contenido):
        if self.size == 0:
            self.head = NodoLiD(contenido=contenido)
            self.size+=1
            return
        nodo = self.head
        nuevo = NodoLiD(contenido= contenido)
        while nodo.siguiente is not None:
            nodo = nodo.siguiente
        nodo.siguiente=nuevo
        nuevo.anterior=nodo
        self.size+=1
           
            
    def imprimir(self):
        nodo= self.head
        while nodo.siguiente is not None:
            print(nodo.contenido, end ="=>")
            nodo = nodo.siguiente
        print(nodo.contenido, end ="=>")
        print()
        while nodo is not None:
            print(nodo.contenido, end ="=>")
            nodo = nodo.anterior
    print("el numero de telefono no existe!!")
    
    def buscar_delvolv(self, valor):
        nodo= self.head
        while nodo is not None:
            if str(nodo.contenido.annio)==str(valor):
                return nodo
            nodo = nodo.siguiente
        return None