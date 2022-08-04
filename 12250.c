#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	int cont=0;
	char tmp[15];
	
	while(scanf("%s", tmp)) {
		if(strcmp(tmp,"#")==0)return 0;
		
		if(strcmp(tmp,"HELLO")==0){
			printf("Case %d: ENGLISH\n",++cont);
		}
		else if(strcmp(tmp,"HOLA")==0){
			printf("Case %d: SPANISH\n",++cont);
		}
		else if(strcmp(tmp,"HALLO")==0){
			printf("Case %d: GERMAN\n",++cont);
		}
		else if(strcmp(tmp,"BONJOUR")==0){
			printf("Case %d: FRENCH\n",++cont);
		}
		else if(strcmp(tmp,"CIAO")==0){
			printf("Case %d: ITALIAN\n",++cont);
		}
		else if(strcmp(tmp,"ZDRAVSTVUJTE")==0){
			printf("Case %d: RUSSIAN\n",++cont);
		}
		else
			printf("Case %d: UNKNOWN\n",++cont);
	}
}
