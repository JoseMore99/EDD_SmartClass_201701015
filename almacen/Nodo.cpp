#ifndef NODO_H
#define NODO_H
#include <iostream>
#include "stdlib.h"
#include "..\estudiante.cpp"

using namespace std;

class Nodo
{
private:
    /* data */
public:
    estudiante *estu;
    Nodo * siguiente;
    Nodo * anterior;
    Nodo(estudiante*);
    
};

Nodo::Nodo (estudiante *e)
{
    this->estu=e;
    this->siguiente=NULL;
    this->anterior = NULL;
}
#endif