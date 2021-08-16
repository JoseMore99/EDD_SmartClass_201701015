#ifndef NodoCola_H
#define NodoCola_H
#include <iostream>
#include "stdlib.h"

using namespace std;

template<typename T>
class NodoCola
{
private:
    /* data */
public:
    T error;
    NodoCola * siguiente;
    NodoCola(T);
    
};

template<typename T>
NodoCola<T>::NodoCola(T e)
{
    this->error=e;
    this->siguiente=NULL;
}
#endif