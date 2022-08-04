#include <stdio.h>
#include <stdlib.h>



int main(){

  int casos = 0;

  scanf("%d", &casos);
  while (casos--) {
    int segmentos = 0, it = 0, cont = 0;
    double **intervalos, abcisas[10000];
    scanf("%d", &segmentos);
    intervalos = (double**) malloc(sizeof(double*)*segmentos);


    while (segmentos--) {
      double x1 = 0, y1 = 0, x2 = 0, y2 = 0, r = 0;
      scanf("%lf %lf %lf %lf %lf", &x1, &y1, &x2, &y2, &r);
      intervalos[it] = (double*) malloc(sizeof(double)*3);

      if (x1 <= x2) {
        intervalos[it][0] = x1;
        intervalos[it][1] = x2;

      }
      else{
        intervalos[it][0] = x2;
        intervalos[it][1] = x1;
      }
      intervalos[it][2] = r;
      it++;

    }
    int l;
    for (l = 0; l < it; l++) {
      abcisas[cont++] = intervalos[l][0];
      abcisas[cont++] = intervalos[l][1];
    }


    int i, j;
    for (i = 0; i < cont; i++) {
      int min = i;
      double  temp = 0;
      for (j = i + 1; j < cont; j++) {
        if (abcisas[j] < abcisas[min]) {
          min = j;
        }
      }
      temp = abcisas[i];
      abcisas[i] = abcisas[min];
      abcisas[min] = temp;
    }

    printf("%d\n-inf %.3lf 1.000\n", cont + 1, abcisas[0]);
    int q = 0;
    while (q < cont - 1) {
      int f;
      double precision = 1;
      for (f = 0; f < it; f++) {
        if (abcisas[q] >= intervalos[f][0] && abcisas[q + 1] <= intervalos[f][1]) {
          precision *= intervalos[f][2];
        }
      }

      printf("%.3lf %.3lf %.3lf\n", abcisas[q], abcisas[q + 1], precision);
      q++;
    }
    printf("%.3lf +inf 1.000\n", abcisas[q]);
    if (casos != 0)printf("\n");

  }

  return 0;
}
