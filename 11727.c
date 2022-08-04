#include <stdio.h>

int main(){
	int casos, primer, medio, ult;
	int caso = 1;
	scanf("%d", &casos);
	while(casos--){
		scanf("%d %d %d", &primer, &medio, &ult);
		if(primer < medio && medio < ult)
			printf("Case %d: %d\n", caso++, medio);
		if(primer > medio && medio > ult)
			printf("Case %d: %d\n", caso++, medio);
		if(primer < medio && primer > ult)
			printf("Case %d: %d\n", caso++, primer);
		if(primer > medio && primer < ult)
			printf("Case %d: %d\n", caso++, primer);
		if(ult < medio && ult > primer)
			printf("Case %d: %d\n", caso++, ult);
		if(ult > medio && ult < primer)
			printf("Case %d: %d\n", caso++,ult);
	}
	return 0;
}

