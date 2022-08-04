#include <stdio.h>
#include <math.h>

int main(){
	long long int casos, guerreros, filas, filasTotal;
	scanf("%lld", &casos);
	while(casos--){
		scanf("%lld", &guerreros);
		filas = sqrt(1 + (8*guerreros));
		filasTotal = (filas-1)/2;
		printf("%lld\n", filasTotal);
	}
	return 0;
}
