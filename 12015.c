#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main(){
	int casos,relevancia[101],i=0,j=0, h=0,max,k=0;
	char url[105][105];
	scanf("%d",&casos);
	while(casos--){
		i = 0;
		j = 0;
		h = 0;
		max = 0;
		while(i < 10){
			scanf("%s %d/n",url[i],&relevancia[i]);
			i++;
		}
		while(j < 10){
			if(relevancia[j]>=max){
				max=relevancia[j];
			}
			j++;
		}
		printf("Case #%d:\n",++k);
		while(h<10){
			if(relevancia[h]==max){
				printf("%s\n",url[h]);
			}
			h++;
		}
	}
}
