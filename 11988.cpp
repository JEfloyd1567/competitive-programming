#include<iostream>
#include<string.h>
#include<list>
using namespace std;

int main(){
	list<char>contenedor;
	string cadena;
	list<char>::iterator iterador = contenedor.begin(); 
	//list<char>::iterator iterador = lista.end() // Final de la lista
    //iterador = lista.begin() // Inicio de la lista
    //lista.insert(iterador, caracter) // Inserta en la lista el elemento caracter sobre la posición que se encuentre el iterador, en este caso al inicio de la lista.
	while (cin>>cadena){
        contenedor.clear();
		for(int i = 0; i < cadena.size(); i++){
            if(cadena[i]=='['){
                iterador = contenedor.begin();
            }
            else if(cadena[i]==']'){
                iterador = contenedor.end();
            }
            else{
                contenedor.insert(iterador,cadena[i]);
            }
        }
        for(iterador=contenedor.begin(); iterador != contenedor.end(); iterador++){
        	cout << *iterador;
        }
        cout<<"\n";
	}
}
