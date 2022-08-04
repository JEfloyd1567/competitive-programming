#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int casos=0,subcasos=0,cont=0,k=0,i;
	char cultivos[110];
	scanf("%d",&casos);
	while(casos--){
		i=0;
		subcasos=0;
		cont=0;
		scanf("%d %s",&subcasos,cultivos);
		while(i<subcasos){
			if(cultivos[i]=='#'){
				i++;
			}
			else{
				cont++;
				i=i+3;
			}
		}
		printf("Case %d: %d\n",++k,cont);
	}
}
