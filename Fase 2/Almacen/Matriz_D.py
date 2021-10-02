
class NodoMatriz():
    def __init__(self, x, y, dato):
        # INICIANDO PUNTEROS Y DATOS DEL NODO
        self.siguiente = None
        self.anterior = None
        self.abajo = None
        self.arriba = None
        self.dato = dato
        self.x = x
        self.y = y

class Matriz():
    def __init__(self):
        self.root = NodoMatriz(-1,-1, "Root")
        self.size=0

    #BUSCA EL NODO CABECERA EN Y
    def buscar_fila(self, y):
        temp = self.root
        while temp is not None:
            if(temp.y == y):
                return temp
            temp = temp.abajo
        return None

    #BUSCA EL NODO CABECERA EN X
    def buscar_columna(self, x):
        temp = self.root
        while temp is not None:
            if(temp.x == x):
                return temp
            temp = temp.siguiente
        return None

    def insertar_ordenado_columna(self, nuevo, cabeza_col):
        temp = cabeza_col
        bandera = False
        while True:
            if(temp.x == nuevo.x):
                # SI LA POSICION ES LA MISMA SOBRE ESCRIBO
                temp.y = nuevo.y
                temp.dato = nuevo.dato
                return temp 
            elif(temp.x > nuevo.x):
                #INSERTAR ANTES DE TEMP
                bandera = True
                break
            if temp.siguiente is not None:
                temp = temp.siguiente
            else:
                # INSERTAR NUEVO DESPUES DE TEMP
                # bandera = FALSE
                break
        if bandera:
            # INSERTAR ANTES DE TEMPORAL
            nuevo.siguiente = temp
            temp.anterior.siguiente = nuevo
            nuevo.anterior = temp.anterior
            temp.anterior = nuevo
        else:
            temp.siguiente = nuevo
            nuevo.anterior = temp
        return nuevo
    
    def insertar_ordenado_fila(self, nuevo, cabeza_fila):
        temp = cabeza_fila
        bandera = False
        while True:
            if(temp.y == nuevo.y):
                # SI LA POSICION ES LA MISMA SOBRE ESCRIBO
                temp.x = nuevo.x
                temp.dato = nuevo.dato
                return temp
            elif(temp.y > nuevo.y):
                #INSERTARLO ANTES DE TEMP
                bandera = True
                break
            if temp.abajo is not None:
                temp = temp.abajo
            else:
                #INSERTAR NUEVO DESPUES DE TEMP
                # bandera = FALSE
                break
        if bandera:
            # INSERTARLO ANTES DE TEMPORAL
            nuevo.abajo = temp
            temp.arriba.abajo = nuevo
            nuevo.arriba = temp.arriba
            temp.arriba = nuevo
        else:
            # INSERCION AL FINAL
            temp.abajo = nuevo
            nuevo.arriba = temp
        return nuevo

    def crear_columna(self, x):
        cabeza_columna = self.root
        columna = self.insertar_ordenado_columna(NodoMatriz(x,-1,"COL"), cabeza_columna)
        return columna

    
    def crear_fila(self, y):
        cabeza_fila = self.root
        fila = self.insertar_ordenado_fila(NodoMatriz(-1,y,"FIL"), cabeza_fila)
        return fila

    # INSERCION GENERAL
    def insertar_elemento(self, x, y, dato):
        self.size+=1
        nuevo = NodoMatriz(x,y,dato)
        NodoColumna = self.buscar_columna(x)
        NodoFila = self.buscar_fila(y)
        # CUANDO COLUMNA NO EXISTA Y FILA NO EXISTA
        if NodoColumna is None and NodoFila is None:
            
            NodoColumna = self.crear_columna(x)
            NodoFila = self.crear_fila(y)
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        #CUANDO COLUNMA NO EXISTA Y FILA EXISTA
        elif NodoColumna is None and NodoFila is not None:

            NodoColumna = self.crear_columna(x)
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        #CUANDO COLUMNA EXISTA Y LA FILA NO EXISTA
        elif NodoColumna is not None and NodoFila is None:
           
            NodoFila = self.crear_fila(y)
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)
            return
        #CUANDO COLUMNA Y LA FILA EXISTEN
        elif NodoColumna is not None and NodoFila is not None:
            nuevo = self.insertar_ordenado_columna(nuevo, NodoFila)
            nuevo = self.insertar_ordenado_fila(nuevo, NodoColumna)

    #BUSQUEDA DE DATOS
    def buscar_dato(self,x,y):
        #BUSCAMOS MEDIANTE LAS COLUMNAS
        temp=self.buscar_columna(x)
        while temp is not None:
            if temp.y==y:
                return temp.dato
            temp = temp.abajo
        return '-'


        