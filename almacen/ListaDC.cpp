#ifndef LISTADC_H
#define LISTADC_H

#include <iostream>
#include <stdlib.h>
#include "Nodo.cpp"
#include "..\estudiante.cpp"

class ListaDC   //LISTA DOBLEMENTE CIRCULAR
{
private:
    /* data */
public:
    Nodo * primero;
    Nodo * ultimo;
    int tamanio;
    ListaDC(/* args */);
    void insertar(estudiante *e);
    bool buscar(int);
};

ListaDC::ListaDC(/* args */)
{
    this->primero = NULL;//VALORES INICIALES DE CABECERAS
    this->ultimo = NULL;
    this->tamanio = 0;
}

void ListaDC::insertar(estudiante *_e){
    Nodo *nuevo = new Nodo(_e);
    if(this->primero == NULL){//EN CASO LA LISTA ESTE VACIA
        this->primero = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    } else{//EN CASO LA LISTA TENGA MINIMO UN VALOR
        nuevo->siguiente = this->primero;
        this->primero->anterior = nuevo;
        nuevo->anterior = this->ultimo;
        this->ultimo->siguiente = nuevo;
        this->ultimo = nuevo;
        this->tamanio++;
    }
    
}

bool ListaDC::buscar(int carnet){
    Nodo *aux = this->primero;
    if (aux->estu->carnet==carnet){
        return true;
    }
    aux = aux->siguiente;
    while (aux!=this->primero)
    {
        if (aux->estu->carnet==carnet){
        return true;
        }
        aux = aux->siguiente;
    }
   return false;
}

/*ListaDC::~ListaDC()
{
}*/

#endif