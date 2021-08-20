#include <iostream>
#ifndef ESTUDIANTE_H
#define ESTUDIANTE_H
using namespace std;

class estudiante
{
private:
    /* data */
public:
    estudiante(int, string, string, string, string, string, int, int); //CONSTRUCTOR
    int carnet, creditos,  edad;
    string nombre, carera, dpi,correo, pass;
};

estudiante::estudiante(int _carnet,string _dpi, string _nombre, string _carrera, string _correo, string _pass, int _creditos, int _edad)
{ //ASIGNACION DE VALORES DEL CONSTRUCTOR
    carnet = _carnet;
    creditos = _creditos;
    dpi = _dpi;
    edad = _edad;
    nombre = _nombre;
    carera = _carrera;
    correo = _correo;
    pass = _pass;
}
#endif