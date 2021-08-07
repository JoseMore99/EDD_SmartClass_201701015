#ifndef LISTADC_H
#define LISTADC_H

#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"

template<typename T>
class ListaDC   //LISTA DOBLEMENTE CIRCULAR
{
private:
    /* data */
public:
    Nodo<T> * primero;
    Nodo<T> * ultimo;
    int tamanio;
    ListaDC(/* args */);
    void insertar(T e);
};

template<typename T>
ListaDC<T>::ListaDC(/* args */)
{
    this->primero = NULL;//VALORES INICIALES DE CABECERAS
    this->ultimo = NULL;
    this->tamanio = 0;
}

template<typename T>
void ListaDC<T>::insertar(T _e){
    Nodo<T> *nuevo = new Nodo<T>(_e);
    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    } else{
        nuevo->siguiente = this->primero;
        this->primero->anterior = nuevo;
        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    }
    
}
/*ListaDC::~ListaDC()
{
}*/

#endif