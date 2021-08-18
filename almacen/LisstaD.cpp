#ifndef LISTAD_H
#define LISTAD_H

#include <iostream>
#include <stdlib.h>
#include "NodoTarea.cpp"

template<typename T>//USO DE TEMPLATE PARA HACER UNA LISTA DE CUALQUIER TIPO
class ListaD   //LISTA DOBLEMENTE 
{
private:
    /* data */
public:
    Nodo<T> * primero;
    Nodo<T> * ultimo;
    int tamanio;
    ListaD(/* args */);
    void insertar(T e);
};

template<typename T>
ListaD<T>::ListaD(/* args */)
{
    this->primero = NULL;//VALORES INICIALES DE CABECERAS
    this->ultimo = NULL;
    this->tamanio = 0;
}

template<typename T>
void ListaD<T>::insertar(T _t){//EN CASO LA LISTA ESTE VACIA
    Nodo<T> *nuevo = new Nodo<T>(_t);
    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    } else{//EN CASO LA LISTA TENGA MINIMO UN VALOR
        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    }
    
}
/*ListaD::~ListaD()
{
}*/

#endif