#include <stdio.h>

int main(){
	int casos, entrada, jugador, i;
	int caso = 1;
	scanf("%d", &casos);
	while(casos--){
		scanf("%d", &entrada);
		int jugadores[entrada];
		for(i = 0; i < entrada; i++){
			scanf("%d", &jugador);
			jugadores[i] = jugador;
		}
		printf("Case %d: %d\n", caso++, jugadores[entrada/2]); 
	}
	return 0;
}