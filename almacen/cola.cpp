#ifndef cola_H
#define cola_H

#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"

template<typename T>
class cola   //LISTA COLA
{
private:
    /* data */
public:
    Nodo<T> * primero;
    Nodo<T> * ultimo;
    int tamanio;
    cola(/* args */);
    void Queue(T e);
    void Dequeue();
    void imprimir();
};

template<typename T>
cola<T>::cola(/* args */)
{
    this->primero = NULL;//VALORES INICIALES DE CABECERAS
    this->ultimo = NULL;
    this->tamanio = 0;
}

template<typename T>
void cola<T>::Queue(T _e){
    Nodo<T> *nuevo = new Nodo<T>(_e);
    if(this->primero == NULL){
        this->primero = nuevo;
        this->ultimo = nuevo;
    } else{
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
    }
    
    this->tamanio++;
}

template<typename T>
void cola<T>::Dequeue(){
    T valor = this->primero->estu;
    Nodo<T> *aux = primero;
    if (this->primero == this->ultimo){
        this->primero= NULL;
        this->ultimo= NULL;
    } else{
        this->primero = this->primero->siguiente;
    }
    delete aux;
}

template<typename T>
void cola<T>::imprimir(){
    Nodo<T> *aux = primero;
    while (aux!=NULL)
    {
        cout<<aux->estu<<"=>";
        aux = aux->siguiente;
    }
    cout<<endl;
    
}

/*ListaDC::~ListaDC()
{
}*/

#endif