#include <stdio.h>
#include <math.h>
#include <string.h>
#include <stdlib.h>

int main(){

  int volume = 0;
  double baking = 0;
  while(scanf("%d %lf", &volume, &baking)){
    if (volume == 0 && baking == 0)break;
    int cant[volume], i, x = 0, ban = 0, p;
    double aux = 0, list[volume], div = 1.0;

    if(baking >= volume)printf("0\n");
    else{
      for(i = 0; i < volume; i++){
        aux = (volume/div) - baking;
        if(aux > 0){
          list[x] = div * 0.3 * sqrt(aux);
          cant[x++] = (int)div;
        }
        div++;
      }
      double mayor = list[0];
      int k, pos = 0, t;

      for(k = 1; k < x; k++){
        if(list[k] > mayor){
          mayor = list[k];
          pos = k;
        }
      }
      char casting[x][50], casteado[50];
      sprintf(casteado, "%lf", mayor);
      for (t = 0; t < x; t++) {
        sprintf(casting[t], "%lf", list[t]);
      }

      for (p = 0; p < x; p++) {
        if (strcmp(casting[p], casteado) == 0 && p != pos)ban = 1;
      }

      if(ban == 0)printf("%d\n", cant[pos]);
      else printf("0\n");
    }

  }
  return 0;
}
