#include <stdio.h>
#include <string.h>
#include <stdlib.h>


int main(){

  int cartas = 0;
  while (scanf("%d", &cartas)){

    if (cartas == 0)break;
    char baraja[cartas + 1][20], mov[cartas + 1][21], position[cartas + 1][21];
    int pos, conteo = 0, k = 1,  it = 1, i = 1, size  = cartas + 1, x = 1, t = 1, band = 1;

    while (cartas--) {
      scanf("%s %s", baraja[it], mov[it]);
      it++;
    }
    for (t = 1; t < size; t++) {
      strcpy(position[t],"-1");
    }
    while (i < it) {
      pos = strlen(mov[i]);
      conteo = 0;
      band = 1;
      while ( 1 ) {
        if (strcmp(position[k],"-1") == 0){
          band = 0;
          conteo++;
        }
        if (conteo == pos)break;
        else if(k == size - 1)k = -1;
        k++;
      }
      strcpy(position[k],baraja[i]);
      i++;
    }
    for (x = 1; x < it; x++) {
      if (x != it-1)printf("%s ", position[x]);
      else printf("%s", position[x]);
    }
    printf("\n");
  }
  return 0;
}
