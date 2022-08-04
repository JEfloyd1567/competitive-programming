#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main(){
	int paredes[100],casos,numParedes,i=0,k=0,j=1,cont=0,cont2=0;
	scanf("%d",&casos);
	while(casos--){
		numParedes=0;
		i=0;
		j=1;
		cont=0;
		cont2=0;
		k++;
		scanf("%d",&numParedes);
		for(i=0;i<numParedes;i++){
			scanf("%d",&paredes[i]);			
		}
		for(j=1;j < numParedes; j++){
			if(paredes[j] > paredes[j-1]){
				cont++;
			}
			if(paredes[j-1] > paredes[j]){
				cont2++;
			}
		}
		printf("Case %d: %d %d\n",k,cont,cont2);
	}
}
