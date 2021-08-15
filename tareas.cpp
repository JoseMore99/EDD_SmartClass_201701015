#include <iostream>

using namespace std;

class tareas
{
private:
    /* data */
public:
    tareas(int,int,  string, string, string, string, string, string); //CONSTRUCTOR
    int id, carnet  ;
    string nombre, materia, descripcion,fecha, hora,estado;
};

tareas::tareas(int _id, int _carnet, string _nombre, string _descripcion,  string _materia, string _fecha, string _hora,string _estado)
{ //ASIGNACION DE VALORES DEL CONSTRUCTOR
    id = _id;
    carnet = _carnet;
    descripcion = _descripcion;
    estado = _estado;
    nombre = _nombre;
    materia = _materia;
    fecha = _fecha;
    hora = _hora;
}
