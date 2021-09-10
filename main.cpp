#include <iostream>
#include <sstream>
#include <stdlib.h>
#include "./almacen/ListaDC.cpp"
#include "./almacen/LisstaD.cpp"
#include "./almacen/cola.cpp"
#include "./almacen/NodoCola.cpp"
#include "./almacen/NodoTarea.cpp"
#include "./almacen/Nodo.cpp"
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
bool verificar_fecha(string);
void graficar_errores();
void graficar_estudiantes();
void graficar_tareas();
void reportes();
void codigo_salida();
int contadorERROR = 0;
int contadorTAREA = 0;
ListaDC *List_estudiantes= new ListaDC();
ListaD *List_tareas= new ListaD();
cola<errores*> *Cola_error = new cola<errores*>();
tareas *cubotarea [5][30][8];
ListaDC*prueba= new ListaDC();
int imgtarea = 1;
int imgestu = 1;


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
                CargarTareas();
                break;
            case 3:
                cout<<"Manual"<<endl;
                ingreso_manual();
                break;
            case 4:
                cout<<"Reportes"<<endl;
                reportes();

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
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Letra incluida en el carnet de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        if (carnet.length()!=9){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Mala estructura en el carnet de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,dpi,',');
        if (verificar_num(dpi)){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Letra incluida en el dpi de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        if (dpi.length()!=13){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Mala estructura en el dpi de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,nombre,',');
        getline(strim,carera,',');
        getline(strim,pass,',');
        getline(strim,creditos,',');
        if (verificar_num(creditos)){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Letra incluida en los creditos de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,edad,',');
        if (verificar_num(edad)){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Letra incluida en la edad de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        getline(strim,correo,',');
        if (verificar_correo(correo)){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Estudiante","Mala estructura del correo de la linea "+ to_string(contador));
            Cola_error->Queue(newerror);
        }
        int carnint = stoi(carnet);
        int credint =stoi(creditos);
        int edadint= stoi(edad);
        estudiante *nuevo = new estudiante(carnint,dpi,nombre, carera, correo, pass,credint,edadint);
        List_estudiantes->insertar(nuevo);
        cout<<List_estudiantes->tamanio<<"=>"<<Cola_error->tamanio<<endl;
    }
    

    archi.close();

}

void CargarTareas(){
fstream archi;
string ruta;
string fila;
string nombre, materia, descripcion,fecha, hora,estado,id, carnet;
string mes,dia;
cout<<"INGRESE RUTA DEL ARCHIVO DE TAREAS:"<<endl;
    cin>>ruta;
    archi.open(ruta, ios::in);//ABRIR ARCHIVO PARA LEER
    if(archi.fail()){
        cout<<"RUTA ERRONEA"<<endl;
    }
    getline(archi,fila);
    while (getline(archi,fila))
    {
        contadorTAREA++;
        stringstream strim(fila);
        getline(strim,mes,',');
        getline(strim,dia,',');
        getline(strim,hora,',');
        getline(strim,carnet,',');
        getline(strim,nombre,',');
        getline(strim,descripcion,',');
        getline(strim,materia,',');
        getline(strim,fecha,',');
        if (verificar_fecha(fecha)){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Tarea","Estructura mala de la fecha en la linea "+ to_string(contadorTAREA));
            Cola_error->Queue(newerror);
        }
        getline(strim,estado,',');
        int carnint = stoi(carnet);
        if (List_estudiantes->buscar(carnint)!=true){
            contadorERROR++;
            errores *newerror = new errores(contadorERROR,"Tarea"," No encontrado en la lista de estudiantes el carnet de la fila "+ to_string(contadorTAREA));
            Cola_error->Queue(newerror);
        }
        int mesint = stoi(mes);
        int diaint= stoi (dia);
        int horaint = stoi(hora);
        int pocision=(horaint*30+diaint)*5+mesint;
        tareas *nueva = new tareas(contadorTAREA,carnint,nombre, descripcion,materia,fecha, horaint,estado,pocision);
        cubotarea[mesint-6][diaint][horaint]=nueva;
        //cout<<materia<<"=>";
        List_tareas->insertar(nueva);
    }
    
    List_tareas->imprimir();
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
            string dipi;
            cout<<"Ingresar Dpi:";
            cin>>dipi;
            List_estudiantes->eliminar(dipi);
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
        int carnet , hora,mes, dia ;
        string nombre, materia, descripcion,fecha,estado;
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
                cout<<"Ingresar Mes"<<endl;
                cin>>mes;
                cout<<"Ingresar dia"<<endl;
                cin>>dia;
                cout<<"Ingresar hora:"<<endl;
                cin>>hora;
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
                cout<<"Ingresar estado:"<<endl;
                cin>>estado;
                contadorTAREA++;
                int pocision =(dia*30+hora)*5+mes;;
                tareas *nueva = new tareas(contadorTAREA,carnet,nombre, descripcion,materia,fecha, hora,estado, pocision);
                cout<<"INGREADO!!"<<endl;}
                break;
            case 2:
                cout<<"MODIFICADO!!"<<endl;
                break;
            case 3:
                int oci;
                cout<<"Ingresar pocision:";
                cin>>oci;
                List_tareas->eliminar(oci);
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
             cout<<"ERROR N"<<endl;
         }
     }
        return false;
}

bool verificar_correo(string val){
    if (regex_match(val, regex("([a-zA-Z]+)([_.a-zA-Z0-9]*)([a-zA-Z0-9]+)(@)([a-zA-Z]+)([.a-zA-Z]+)([a-zA-Z]+)"))){
        return false;
    } 
    cout<<"ERROR C"<<endl;
    return true;
}

bool verificar_fecha(string val){
  if (regex_match(val, regex("([0-9])([0-9])([0-9])([0-9])(/)([0-9])([0-9])(/)([0-9])([0-9])"))){
        return false;
    } 
    cout<<"ERROR C"<<endl;
    return true;
}

void reportes(){
    int opci;
    cout<<"++++++REPORTES+++++++"<<endl;
    cout<<"1. Reporte sobre la lista de estudiantes"<<endl;
    cout<<"2. Reporte sobre la lista de tareas linealizadas"<<endl;
    cout<<"3. Busqueda en estructura linealizada."<<endl;
    cout<<"4. Busqueda de posicion en lista linealizada"<<endl;
    cout<<"5. Cola de Errores"<<endl;
    cout<<"6. Codigo generado de salida"<<endl;
    cout<<"+++++++++++++++++++++++++"<<endl;
    cout<<"ingrese una opcion: ";
    cin>>opci;
    switch (opci)
    {
    case 1:
        graficar_estudiantes();
        break;
    case 2:
        graficar_tareas();
        break;
    case 3:{
        int mes,  dia, hora;
        cout<<"Ingresar Mes"<<endl;
        cin>>mes;
        cout<<"Ingresar dia"<<endl;
        cin>>dia;
        cout<<"Ingresar hora:"<<endl;
        cin>>hora;
        List_tareas->buscar(mes,dia,hora);
    }
        break;
    case 4:{
        int mes,  dia, hora;
        cout<<"Ingresar Mes"<<endl;
        cin>>mes;
        cout<<"Ingresar dia"<<endl;
        cin>>dia;
        cout<<"Ingresar hora:"<<endl;
        cin>>hora;
        int este =(dia*30+hora)*5+mes;;
        cout<<"La pocision de esta tarea es:"<<este<<endl;
    }
        break;
    case 5:
        graficar_errores();
        break;
    case 6:
        codigo_salida();
        break;
    default:
    cout<<"Seleccione una opcion correcta"<<endl;
        break;
    }
    
}

void graficar_errores(){
    ofstream archi;
    archi.open("Errores.dot",ios::out);
    int contadornodo = 0;
    if(archi.fail()){
     cout<<"Ocurrio un error inesperado"<<endl;
     return;
    }
    archi<<"digraph g {\ngraph [];\nnode [\nfontsize = \"16\"\nshape = \"ellipse\"\n];\nedge [];"<<endl;
    NodoCola<errores*> *aux = Cola_error->primero;
    while (aux != NULL){
        archi<<"nodo"<<contadornodo<<"[label=\" ";
        archi<<"id:"<<aux->error->id;
        archi<<"\\nTipo"<<aux->error->tipo;
        archi<<"\\ndescripcion:"<<aux->error->descripcion<<"\"];"<<endl;
        contadornodo++;
        aux = aux->siguiente;
    }
    cout<<"GRAFICA REALIZADA CON EXITO"<<endl;
    for (int i = 0; i < contadornodo-1; i++){
        int j = i+1;
        archi<<"nodo"<<i<<"->"<<"nodo"<<j<<endl;
    }
    
    archi<<"}";
    archi.close();
    string cmd = "dot -Tpng Errores.dot -o Errores.png";
    system(cmd.c_str());    
}

void graficar_estudiantes(){
    ofstream archi;
    archi.open("Estudiantes.dot",ios::out);
    int contadornodo = 0;
    if(archi.fail()){
     cout<<"Ocurrio un error inesperado"<<endl;
     return;
    }
    archi<<"digraph g {\ngraph [\nrankdir = \"LR\"\n];\nnode [\nfontsize = \"16\"\nshape = \"ellipse\"\n];\nedge [];"<<endl;
    Nodo *aux = List_estudiantes->primero;
    do {
        archi<<"nodo"<<contadornodo<<"[label=\" ";
        archi<<"carnet:"<<aux->estu->carnet;
        archi<<"\\ndpi:"<<aux->estu->dpi;
        archi<<"\\nnombre:"<<aux->estu->nombre;
        archi<<"\\ncarrera:"<<aux->estu->carera;
        archi<<"\\npassword:"<<aux->estu->pass;
        archi<<"\\ncreditos:"<<aux->estu->creditos;
        archi<<"\\nedad:"<<aux->estu->edad<<"\"];"<<endl;
        contadornodo++;
        aux = aux->siguiente;
    }while (aux != List_estudiantes->primero);
    cout<<"GRAFICA REALIZADA CON EXITO"<<endl;
    for (int i = 0; i < contadornodo-1; i++){
        int j = i+1;
        archi<<"nodo"<<i<<"->"<<"nodo"<<j<<endl;
        archi<<"nodo"<<j<<"->"<<"nodo"<<i<<endl;
    }

    archi<<"nodo0->"<<"nodo"<<(contadornodo-1)<<endl;
    archi<<"nodo"<<(contadornodo-1)<<"->"<<"nodo0"<<endl;
    archi<<"}";
    archi.close();
    string cmd = "dot -Tpng Estudiantes.dot -o Estudiantes"+to_string(imgestu)+".png";
    imgestu++;
    system(cmd.c_str());    
}

void graficar_tareas(){
    ofstream archi;
    archi.open("Tareas.dot",ios::out);
    int contadornodo = 0;
    if(archi.fail()){
     cout<<"Ocurrio un error inesperado"<<endl;
     return;
    }
    archi<<"digraph g {\ngraph [\nrankdir = \"LR\"\n];\nnode [\nfontsize = \"16\"\nshape = \"square\"\n];\nedge [];"<<endl;
    NodoTarea *aux = List_tareas->primero;
    while (aux != NULL){
        archi<<"nodo"<<contadornodo<<"[label=\" ";
        archi<<"Pocision:"<<aux->tarea->pocision;
        archi<<"carnet:"<<aux->tarea->carnet;
        archi<<"\\nnombre:"<<aux->tarea->nombre;
        archi<<"\\ndescripcion:"<<aux->tarea->descripcion;
        archi<<"\\nmateria:"<<aux->tarea->materia;
        archi<<"\\nfecha:"<<aux->tarea->fecha;
        archi<<"\\nestado:"<<aux->tarea->estado<<"\"];"<<endl;
        contadornodo++;
        aux = aux->siguiente;
    }
    cout<<"GRAFICA REALIZADA CON EXITO"<<endl;
    for (int i = 0; i < contadornodo-1; i++){
        int j = i+1;
        archi<<"nodo"<<i<<"->"<<"nodo"<<j<<endl;
        archi<<"nodo"<<j<<"->"<<"nodo"<<i<<endl;
    }
    archi<<"}";
    archi.close();
    string cmd = "dot -Tpng Tareas.dot -o Tareas"+to_string(imgtarea)+".png";
    imgtarea++;
    system(cmd.c_str());    
}

void codigo_salida(){
    ofstream archi;
    archi.open("Estudiantes.txt",ios::out);
    if(archi.fail()){
     cout<<"Ocurrio un error inesperado"<<endl;
     return;
    }
    archi<<"¿Elements?"<<endl;
    Nodo *aux = List_estudiantes->primero;
    do {
        archi<<"    ¿element type=\"user\"?"<<endl;
        archi<<"        ¿item Carnet=\""<<aux->estu->carnet<<"\"$?"<<endl;
        archi<<"        ¿item Dpi=\""<<aux->estu->dpi<<"\"$?"<<endl;
        archi<<"        ¿item Nombre=\""<<aux->estu->nombre<<"\"$?"<<endl;
        archi<<"        ¿item Carrera=\""<<aux->estu->carera<<"\"$?"<<endl;
        archi<<"        ¿item Password=\""<<aux->estu->pass<<"\"$?"<<endl;
        archi<<"        ¿item Creditos=\""<<aux->estu->creditos<<"\"$?"<<endl;
        archi<<"        ¿item Edad=\""<<aux->estu->edad<<"\"$?"<<endl;
        archi<<"    ¿$element?"<<endl;
        aux = aux->siguiente;
    }while (aux != List_estudiantes->primero);
    NodoTarea *aux2 = List_tareas->primero;
    string anio,mes,dia, fecha;
    
    while (aux2 != NULL)
    {
        fecha = aux2->tarea->fecha;
        stringstream strim(fecha);
        getline(strim,anio,'/');
        getline(strim,mes,'/');
        getline(strim,dia,'/');
        archi<<"    ¿element type=\"task\"?"<<endl;
        archi<<"        ¿item Carnet=\""<<aux2->tarea->carnet<<"\"$?"<<endl;
        archi<<"        ¿item Nombre=\""<<aux2->tarea->nombre<<"\"$?"<<endl;
        archi<<"        ¿item Descripcion=\""<<aux2->tarea->descripcion<<"\"$?"<<endl;
        archi<<"        ¿item Materia=\""<<aux2->tarea->materia<<"\"$?"<<endl;
        archi<<"        ¿item Fecha=\""<<dia<<"/"<<mes<<"/"<<anio<<"\"$?"<<endl;
        archi<<"        ¿item Hora=\""<<aux2->tarea->hora<<"\"$?"<<endl;
        archi<<"        ¿item Estado=\""<<aux2->tarea->estado<<"\"$?"<<endl;
        archi<<"    ¿$element?"<<endl;
        aux2 = aux2->siguiente;
    }
    
    archi<<"¿$Elements?";
    cout<<"ARCHIVO DE SALIDA REALIZADO CON EXITO"<<endl;
   
}