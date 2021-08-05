#include <iostream>
#include "stdlib.h"

using namespace std;

template<typename T>
class Nodo
{
private:
    /* data */
public:
    Nodo(T);
    T estu;
    Nodo * siguiente;
    Nodo * anterior;
};

template<typename T>
Nodo<T>::Nodo(T e)
{
    this->estu=e;
    this->siguiente=NULL;
    this->anterior = NULL;
}