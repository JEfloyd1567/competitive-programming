#include <stdio.h>

int main(){
	int casos, subCasos, casosCompra, costo;
	char fabricantes[10000][21];
	int menor[1000000], mayor[1000000]; 
	int i, j;
	scanf("%d", &casos);
	while(casos--){
		scanf("%d", &subCasos);
		for(i = 0; i < subCasos; i++){
			scanf("%s %d %d", fabricantes[i], &menor[i], &mayor[i]);
		}
		scanf("%d", &casosCompra);
		while(casosCompra--){
			int contador = 0, aux = 0;
			scanf("%d", &costo);
			for(j = 0; j < subCasos; j++){
				if((menor[j] <= costo) && (costo <= mayor[j])){
					contador++;
					aux = j;
				}
			}
			if(contador == 1)
				printf("%s\n", fabricantes[aux]);
			else
				printf("UNDETERMINED\n");
		}
		if(casos)
			printf("\n");
	}
	return 0;
}
