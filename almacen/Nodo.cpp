#ifndef NODO_H
#define NODO_H
#include <iostream>
#include "stdlib.h"

using namespace std;

template<typename T>
class Nodo
{
private:
    /* data */
public:
    T estu;
    Nodo * siguiente;
    Nodo * anterior;
    Nodo(T);
    
};

template<typename T>
Nodo<T>::Nodo(T e)
{
    this->estu=e;
    this->siguiente=NULL;
    this->anterior = NULL;
}
#endif