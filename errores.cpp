#include <iostream>

using namespace std;

class errores
{
private:
    /* data */
public:
    errores(int,string, string);
    int id  ;
    string tipo, descripcion;
};

errores::errores(int _id, string _tipo, string _descripcion)
{
    id = _id;
    descripcion = _descripcion;
    tipo = _tipo;
}

