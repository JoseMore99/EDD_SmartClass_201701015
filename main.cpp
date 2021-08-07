#include <iostream>
#include "./almacen/ListaDC.cpp"
#include "estudiante.cpp"

using namespace std;

void ingreso_manual();
void manual_usu();
void manual_tare();
ListaDC<estudiante> *List_estudiantes= new ListaDC<estudiante>();
ListaDC<int> *prueba= new ListaDC<int>();

int main(){
    
    int opcion;
    while (opcion !=5)
    {
        cout<<"++++++++++MENU+++++++++++"<<endl;
        cout<<"1. Carga de Usuarios"<<endl;
        cout<<"2. Carga de Tareas"<<endl;
        cout<<"3. Ingreso Manual"<<endl;
        cout<<"4. Reportes"<<endl;
        cout<<"5. Salir"<<endl;
        cout<<"+++++++++++++++++++++++++"<<endl;
        cout<<"ingrese una opcion: ";
        cin>>opcion;
        switch (opcion)
            {
            case 1:
                cout<<"Usuarios"<<endl;
                break;
            case 2:
                cout<<"tareas"<<endl;
                break;
            case 3:
                cout<<"Manual"<<endl;
                ingreso_manual();
                break;
            case 4:
                cout<<"Repportes"<<endl;
                break;
            case 5:
                cout<<"FIN"<<endl;
                break;
            default:
                cout<<"Seleccione una opcion correcta"<<endl;
                break;
            }
        
    }

    system("pause");
    return 0;
}

void ingreso_manual(){
    int opci;
    while (opci !=3)
    {
        cout<<"++++++INGRESO MANUAL+++++++"<<endl;
        cout<<"1. Carga de Usuarios Manualmente"<<endl;
        cout<<"2. Carga de Tareas Manualmente"<<endl;
        cout<<"3. Regresar"<<endl;
        cout<<"+++++++++++++++++++++++++"<<endl;
        cout<<"ingrese una opcion: ";
        cin>>opci;
        switch (opci)
        {
        case 1:
            manual_usu();
            break;
        case 2:
            manual_tare();
            break;
        default:
        cout<<"Seleccione una opcion correcta"<<endl;
            break;
        }
    }
    
}

void manual_usu(){
    int opc;
    int carnet, creditos, dpi, edad;
    string nombre, carera, correo, pass;
    while (opc !=4)
    {
        cout<<"++++++USUARIO MANUAL+++++++"<<endl;
        cout<<"1. Ingresar"<<endl;
        cout<<"2. Modificar"<<endl;
        cout<<"3. Eliminar"<<endl;
        cout<<"4. Regrear"<<endl;
        cout<<"+++++++++++++++++++++++++"<<endl;
        cout<<"ingrese una opcion: ";
        cin>>opc;
        switch (opc)
        {
        case 1:
            cout<<"Ingresar Carnet:"<<endl;
            cin>>carnet;
            cout<<"Ingresar dpi:"<<endl;
            cin>>dpi;
            cout<<"Ingresar Carnet:"<<endl;
            cin>>carnet;
            cout<<"Ingresar Carnet:"<<endl;
            cin>>carnet;
            cout<<"INGREADO!!"<<endl;
            break;
        case 2:
            cout<<"MODIFICADO!!"<<endl;
            break;
        case 3:
            cout<<"ELIMINADO!!"<<endl;
            break;
        default:
        cout<<"Seleccione una opcion correcta"<<endl;
            break;
        }
    }
    
}

void manual_tare(){
    int opc;
    while (opc !=4)
    {
        cout<<"++++++TAREA MANUAL+++++++"<<endl;
        cout<<"1. Ingresar"<<endl;
        cout<<"2. Modificar"<<endl;
        cout<<"3. Eliminar"<<endl;
        cout<<"4. Regrear"<<endl;
        cout<<"+++++++++++++++++++++++++"<<endl;
        cout<<"ingrese una opcion: ";
        cin>>opc;
        switch (opc)
        {
        case 1:
            cout<<"INGREADO!!"<<endl;
            break;
        case 2:
            cout<<"MODIFICADO!!"<<endl;
            break;
        case 3:
            cout<<"ELIMINADO!!"<<endl;
            break;
        default:
        cout<<"Seleccione una opcion correcta"<<endl;
            break;
        }
    }
    
}