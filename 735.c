#include <stdio.h>
#include <stdlib.h>

int compare(const void* x, const void* y){
  int *a = (int*)x;
  int *b = (int*)y;

  if (*a < *b)return -1;
  else if(*a > *b)return 1;
  else return 0;
}
int main(){

  int x[1000], size = 0;
  for (size_t i = 1; i <= 20; i++) {
    for (size_t k = 1; k <= 3; k++) {
      x[size++] = i * k;

    }
  }
  qsort(x, size, sizeof(int), compare);
  for (size_t i = 0; i < size; i++) {
    printf("%d, ", x[i]);
  }
  printf("\n%d\n",size );
  return 0;
}
