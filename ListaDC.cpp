#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"

template<typename T>
class ListaDC
{
private:
    /* data */
public:
    Nodo<T> * primero;
    Nodo<T> * ultimo;
    ListaDC(/* args */);
    int tamaño;
    void insertar(T e)
    ~ListaDC();
};

template<typename T>
ListaDC<T>::ListaDC(/* args */)
{
    this->primero = NULL;
    this->ultimo = NULL;
    this->tamaño = 0;
}

template<typename T>
void ListaDC<T>::insertar(T _e){
    Nodo<T> *nuevo = new Nodo<T>(_e)
    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
    } else{
        nuevo->siguente = this->siguiente;

    }
    
}
/*ListaDC::~ListaDC()
{
}*/
