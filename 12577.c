#include <stdio.h>
#include <string.h>

int main(){
	char arr[6];
	char hajj[5] = "Hajj";
	char umrah[6] = "Umrah";
	char arr1[] = "*";
	int casos = 1;
	while(scanf("%s", arr) && strcmp(arr, arr1) != 0){
		if(strcmp(arr, hajj) == 0){
			printf("Case %d: Hajj-e-Akbar\n", casos++);		
		}	
		if(strcmp(arr, umrah) == 0){
			printf("Case %d: Hajj-e-Asghar\n", casos++);	
		}
	}
}
