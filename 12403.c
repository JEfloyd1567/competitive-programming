#include <stdio.h>
#include <string.h>

int main(){
	int total = 0;
	int casos, val;
	char palabra[7];
	char report[7] = "report";
	char donate[7] = "donate";
	scanf("%d",  &casos);
	while(casos--){
		scanf("%s", palabra); 
		if(strcmp(palabra, donate) == 0){
			scanf("%d", &val);
			total = total + val;
		}
		if(strcmp(palabra, report) == 0){
			printf("%d\n", total);
		}
	}
	return 0;
}
