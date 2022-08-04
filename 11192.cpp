#include<iostream>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
using namespace std;

int main(){
	int transicion=0,largo=0,prueba=0,limite=0;
	char cadena[102];
	char tmp;
	while(scanf("%d",&prueba)){
		if(prueba==0){
			return 0;
		}
		else{
			scanf("%s",&cadena);
			largo=strlen(cadena);
			transicion=largo/prueba;
			for(int j=0;j<transicion;j+=transicion){
				for(int i=j;i<=transicion/2;i++){ 
					limite=transicion-1-i;
					if(i==limite){
						break; 
					}
					else{
						tmp=cadena[i];
						cadena[i]=cadena[limite];
						cadena[limite]=tmp;
						printf("%s\n",cadena);
					}
				}
			}
		}
		printf("%s\n",cadena);
	}
}
