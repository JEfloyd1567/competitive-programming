#include <stdio.h>

int main() {
  int puntos[] = {0, 1 ,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20
                    , 21, 22, 24, 26, 27, 28, 30, 32, 33, 34, 36, 38, 39, 40, 42, 45, 48, 51, 54, 57, 60, 50};

  int entrada = 0;

  while(scanf("%d", &entrada) != EOF){

    int   it, jt, kt, i, j, k, size = 43;
    int  combination = 0, permutation = 0;

    if (entrada <= 0)break;

    for(it = 0; it < size; it++){
      for(jt = it; jt < size; jt++){
        for(kt = jt; kt < size; kt++){
          if  (puntos[it] + puntos[jt]+ puntos[kt] == entrada ) {
            combination++;
          }
        }
      }
    }
    for(i = 0; i < size; i++){
      for(j = 0; j < size; j++){
        for(k = 0; k < size; k++){
          if  (puntos[i] + puntos[j]+ puntos[k] == entrada ) {
            permutation++;
          }
        }
      }
    }
    if (combination == 0 && permutation == 0 ) {
      printf("THE SCORE OF %d CANNOT BE MADE WITH THREE DARTS.\n", entrada);
      printf("**********************************************************************\n");
    }
    else{
      printf("NUMBER OF COMBINATIONS THAT SCORES %d IS %d.\n", entrada, combination);
      printf("NUMBER OF PERMUTATIONS THAT SCORES %d IS %d.\n", entrada, permutation);
      printf("**********************************************************************\n");
    }
    combination = 0;
    permutation = 0;

  }
  printf("END OF OUTPUT\n");
  return 0;
}
