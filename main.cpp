#include <iostream>
#include <sstream>
#include "./almacen/ListaDC.cpp"
#include "./almacen/LisstaD.cpp"
#include "./almacen/cola.cpp"
#include "estudiante.cpp"
#include "errores.cpp"
#include "tareas.cpp"
#include "string"
#include "fstream"
#include "regex"

using namespace std;

void ingreso_manual();
void manual_usu();
void manual_tare();
void CargarUsuarios();
void CargarTareas();
bool verificar_num(string);
bool verificar_correo(string);
ListaDC<estudiante*> *List_estudiantes= new ListaDC<estudiante*>();
ListaD<tareas*> *List_tareas= new ListaD<tareas*>();
cola<errores*> *Cola_error = new cola<errores*>();
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
                CargarUsuarios();
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

void CargarUsuarios(){
    ifstream archi;
    string ruta;
    string fila;
    string nombre, carera, correo, pass,carnet, creditos, dpi, edad;
    int contador=1;
    cout<<"INGRESE RUTA DEL ARCHIVO DE USUARIOS:"<<endl;
    cin>>ruta;
    archi.open(ruta, ios::in);//ABRIR ARCHIVO PARA LEER
    if(archi.fail()){
        cout<<"RUTA ERRONEA"<<endl;
    }
    getline(archi,fila);
    while (getline(archi,fila))
    {
        contador++;
        stringstream strim(fila);
        getline(strim,carnet,',');
        if (verificar_num(carnet)){
            errores *newerror = new errores(1,carnet,"Letra incluida en el carnet de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        if (carnet.length()!=9){
            errores *newerror = new errores(1,carnet,"Mala estructura en el carnet de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,dpi,',');
        if (verificar_num(dpi)){
            errores *newerror = new errores(1,dpi,"Letra incluida en el dpi de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        if (carnet.length()!=13){
            errores *newerror = new errores(1,carnet,"Mala estructura en el carnet de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,nombre,',');
        getline(strim,carera,',');
        getline(strim,pass,',');
        getline(strim,creditos,',');
        if (verificar_num(creditos)){
            errores *newerror = new errores(1,creditos,"Letra incluida en los creditos de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,edad,',');
        if (verificar_num(edad)){
            errores *newerror = new errores(1,edad,"Letra incluida en la edad de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,correo,',');
        if (verificar_correo(correo)){
            errores *newerror = new errores(1,correo,"Mala estructura del correo de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        int carnint = stoi(carnet);
        int credint =stoi(creditos);
        int edadint= stoi(edad);
        estudiante *nuevo = new estudiante(carnint,dpi,nombre, carera, correo, pass,credint,edadint);
        List_estudiantes->insertar(nuevo);
        cout<<List_estudiantes->tamanio<<endl;
    }
    

    archi.close();

}

void CargarTareas(){
fstream archi;
string ruta;
string fila;
string nombre, materia, descripcion,fecha, hora,estado,id, carnet ;
string mes,dia;
cout<<"INGRESE RUTA DEL ARCHIVO DE USUARIOS:"<<endl;
    cin>>ruta;
    archi.open(ruta, ios::in);//ABRIR ARCHIVO PARA LEER
    if(archi.fail()){
        cout<<"RUTA ERRONEA"<<endl;
    }
    getline(archi,fila);
    while (getline(archi,fila))
    {
        stringstream strim(fila);
        getline(strim,mes,',');
        getline(strim,dia,',');
        getline(strim,hora,',');
        getline(strim,carnet,',');
        getline(strim,nombre,',');
        getline(strim,descripcion,',');
        getline(strim,materia,',');
        getline(strim,fecha,',');
        getline(strim,estado,',');
        int carnint = stoi(carnet);
        
        cout<<materia<<"=>";
    }
    

    archi.close();

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
    int carnet, creditos, edad;
    string nombre, carera, correo,dpi, pass;
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
        {
            cout<<"Ingresar Carnet:"<<endl;
            cin>>carnet;
            cout<<"Ingresar dpi:"<<endl;
            cin>>dpi;
            cout<<"Ingresar Nombre:"<<endl;
            cin>>nombre;
            cout<<"Ingresar Carrera:"<<endl;
            cin>>carera;
            cout<<"Ingresar Correo:"<<endl;
            cin>>correo;
            cout<<"Ingresar Contrasena:"<<endl;
            cin>>pass;
            cout<<"Ingresar Creditos:"<<endl;
            cin>>creditos;
            cout<<"Ingresar Edad:"<<endl;
            cin>>edad;
            estudiante *nuevo = new estudiante(carnet,dpi,nombre, carera, correo, pass,creditos,edad);
            List_estudiantes->insertar(nuevo);
            cout<<List_estudiantes->tamanio<<endl;
            cout<<"INGREADO!!"<<endl;
            }
            break;
        
        case 2:{
            cout<<"MODIFICADO!!"<<endl;
        }break;
        case 3:{
            cout<<"ELIMINADO!!"<<endl;
        }break;
        default:{
        cout<<"Seleccione una opcion correcta"<<endl;
        }break;
        }
    }
    
}

void manual_tare(){
        int opc;
        int id, carnet  ;
        string nombre, materia, descripcion,fecha, hora,estado;
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
            case 1:{
                cout<<"Ingresar Carnet:"<<endl;
                cin>>carnet;
                cout<<"Ingresar nombre:"<<endl;
                cin>>nombre;
                cout<<"Ingresar descripcion:"<<endl;
                cin>>descripcion;
                cout<<"Ingresar Materia:"<<endl;
                cin>>materia;
                cout<<"Ingresar fecha:"<<endl;
                cin>>fecha;
                cout<<"Ingresar hora:"<<endl;
                cin>>hora;
                cout<<"Ingresar estado:"<<endl;
                cin>>estado;
                tareas *nueva = new tareas(id=1,carnet,nombre, descripcion,materia,fecha, hora,estado);
                cout<<"INGREADO!!"<<endl;}
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

bool verificar_num(string val){
    int i = 0;
     char c;
     for (i; i < val.size(); i++)
     {
         c = val[i];
         if(isalpha(c)==1){
             return true;
         }
     }
        return false;
}

bool verificar_correo(string val){
    if (regex_match(val, regex("([a-z]+)([_.a-z0-9]*)([a-z0-9]+)(@)([a-z]+)([.a-z]+)([a-z]+)"))){
        return false;
    } 

    return true;
}