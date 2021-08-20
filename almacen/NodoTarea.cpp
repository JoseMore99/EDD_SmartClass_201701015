#ifndef NODOTarea_H
#define NODOTarea_H
#include <iostream>
#include "stdlib.h"
#include "..\tareas.cpp"

using namespace std;


class NodoTarea
{
private:
    /* data */
public:
    tareas *tarea;
    NodoTarea * siguiente;
    NodoTarea * anterior;
    NodoTarea(tareas*);
    
};

NodoTarea::NodoTarea(tareas *t)
{
    this->tarea=t;
    this->siguiente=NULL;
    this->anterior = NULL;
}
#endif