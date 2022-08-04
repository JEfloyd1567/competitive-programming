#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(){

  int casos = 0;
  scanf("%d\n", &casos);
  while (casos--) {
    char operation[10000], signos[100], number[100];
    long long int numeros[10000];
    scanf("%s", operation);
    int i, it = 0, size = 0, size_sign = 0;
    for (i = 0; operation[i] != '\0'; i++) {
      if (operation[i] != '*' && operation[i] != '+') {
        number[it++] = operation[i];
      }
      else{
        signos[size_sign++] = operation[i];
        numeros[size++] = atoi(number);
        int k = 0;
        while (it--)number[k++] = '\0';
        it = 0;

      }
    }

    numeros[size++] = atoi(number);
    int k1 = 0;
    while (it--)number[k1++] = '\0';
    it = 0;

    long long int suma = 0, a1 = 0, a2 = 0, sum_prod[1000], max = 1;
    int iter = 0, p = 0, f = 0, k;
    a1 = numeros[0];
    for (iter = 1; iter < size; iter++) {
      a2 = numeros[iter];
      if (signos[p] == '+') {
        suma = a1 + a2;
        a1 = suma;
      }
      else{
        sum_prod[f++] = a1;
        a1 = a2;
      }
      p++;
    }
    sum_prod[f++] = a1;

    for (k = 0; k < f; k++) {
      max *= sum_prod[k];
    }

    long long int aux = 0, b1 = 1, b2 = 1, almacen[1000], pt = 0, min = 0;
    int x, cont = 0, q = 0;
    b1 = numeros[0];
    for (cont = 1; cont < size; cont++) {
      b2 = numeros[cont];
      if (signos[pt] == '*') {
        aux = b1 * b2;
        b1 = aux;
      }
      else{
        almacen[q++] = b1;
        b1 = b2;
      }
      pt++;
    }
    almacen[q++] = b1;

    for (x = 0; x < q; x++) {
      min += almacen[x];
    }
    printf("The maximum and minimum are %lld and %lld.\n", max, min);

  }

  return 0;
}
