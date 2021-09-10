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

    def __str__(self):
        print("Carnet: "+self.carnet)
        print("Creditos: "+self.creditos)
        print("Dpi: "+self.dpi)
        print("Edad: "+self.edad)
        print("Nombre: "+self.nombre)
        print("Carrera: "+self.carrera)
        print("Password: "+self.passw)
        return "-------------------"

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