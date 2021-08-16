#ifndef NODOTarea_H
#define NODOTarea_H
#include <iostream>
#include "stdlib.h"

using namespace std;

template<typename T>
class NodoTarea
{
private:
    /* data */
public:
    T tarea;
    NodoTarea * siguiente;
    NodoTarea * anterior;
    NodoTarea(T);
    
};

template<typename T>
NodoTarea<T>::NodoTarea(T t)
{
    this->tarea=t;
    this->siguiente=NULL;
    this->anterior = NULL;
}
#endif