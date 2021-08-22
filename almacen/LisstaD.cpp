#ifndef LISTAD_H
#define LISTAD_H

#include <iostream>
#include <stdlib.h>
#include "NodoTarea.cpp"
#include "..\tareas.cpp"


class ListaD   //LISTA DOBLEMENTE 
{
private:
    /* data */
public:
    NodoTarea * primero;
    int tamanio;
    ListaD(/* args */);
    void insertar(tareas *t);
    void imprimir();
    void buscar(int, int, int);
    void eliminar(int);
};

ListaD::ListaD(/* args */)
{
    this->primero = NULL;//VALORES INICIALES DE CABECERAS
    this->tamanio = 0;
}

void ListaD::insertar(tareas *_t){//EN CASO LA LISTA ESTE VACIA
    NodoTarea *nuevo = new NodoTarea(_t);
    this->tamanio++;
    if(this->primero == NULL){
        this->primero = nuevo;
    } else{//EN CASO LA LISTA TENGA MINIMO UN VALOR INSERTAR EN ORDEN
        NodoTarea *aux = this->primero;
        while (aux!=NULL)
        {
            if (aux->tarea->pocision>nuevo->tarea->pocision){
                cout<<aux->tarea->pocision<<"->"<<nuevo->tarea->pocision<<endl;
                if (aux == this->primero){
                    nuevo->siguiente= aux;
                    aux->anterior=nuevo;
                    this->primero= nuevo;
                }else{
                aux->anterior->siguiente= nuevo;
                nuevo->siguiente=aux;
                nuevo->anterior=aux->anterior;
                aux->anterior = nuevo;}
                return;
            }
            aux = aux->siguiente;
        }
        NodoTarea *aux2 = this->primero;
        while (aux2->siguiente!=NULL)
        {
            aux2 = aux2->siguiente;
        }
        aux2->siguiente= nuevo;
        nuevo->anterior= aux2;
    }
    
}

void ListaD::buscar(int mes, int dia, int hora){
    NodoTarea *aux = this->primero;
    int este =(dia*30+hora)*5+mes;;
    while (aux!=NULL)
    {
        if (aux->tarea->pocision==este){
        cout<<" Carnet=\""<<aux->tarea->carnet<<"\""<<endl;
        cout<<" Nombre=\""<<aux->tarea->nombre<<"\""<<endl;
        cout<<" Descripcion=\""<<aux->tarea->descripcion<<"\""<<endl;
        cout<<" Materia=\""<<aux->tarea->materia<<"\""<<endl;
        cout<<" Fecha=\""<<aux->tarea->fecha<<"\""<<endl;
        cout<<" Hora=\""<<aux->tarea->hora<<"\""<<endl;
        cout<<" Estado=\""<<aux->tarea->estado<<"\""<<endl;
        return ;
        }
        aux = aux->siguiente;
    }
    cout<<"LA TAREA NO EXISTE"<<endl;
}

void ListaD::imprimir(){
    NodoTarea *aux = this->primero;
        while (aux!=NULL)
        {
            cout<<aux->tarea->pocision<<"=>";
            aux = aux->siguiente;
        }
}

void ListaD::eliminar(int este){
    NodoTarea *aux = this->primero;
    while (aux!=NULL)
    {
        if (aux->tarea->pocision==este){
            if(aux == this->primero){
                this->primero =  this->primero->siguiente;
                primero->anterior = NULL;
                delete(aux);
                return;
            }else{
                if (aux->siguiente==NULL){
                    aux->anterior->siguiente ==NULL;
                    delete(aux);
                    return;
                }
                aux->siguiente->anterior = aux->anterior;
                aux->anterior->siguiente =aux->siguiente;
                delete(aux);
            }
        }
        aux = aux->siguiente;
    }
    cout<<"LA TAREA NO EXISTE"<<endl;
}

/*ListaD::~ListaD()
{
}*/

#endif