#include <iostream>
#ifndef TAREAS_H
#define TAREAS_H

using namespace std;

class tareas
{
private:
    /* data */
public:
    tareas(int,int,  string, string, string, string, int, string,int); //CONSTRUCTOR
    int id, carnet, hora,pocision;
    string nombre, materia, descripcion,fecha,estado;
};

tareas::tareas(int _id, int _carnet, string _nombre, string _descripcion,  string _materia, string _fecha, int _hora,string _estado,int _pocision)
{ //ASIGNACION DE VALORES DEL CONSTRUCTOR
    id = _id;
    carnet = _carnet;
    descripcion = _descripcion;
    estado = _estado;
    nombre = _nombre;
    materia = _materia;
    fecha = _fecha;
    hora = _hora;
    pocision = _pocision;
}

#endif