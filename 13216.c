#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

  int casos = 0;
  scanf("%d", &casos);
  int num_casting, i;
  char number[1000];
  while (casos--) {
    num_casting = 0;
    scanf("%s", &number);
    num_casting = number[0] - '0';
    for (i = 1; i < strlen(number); i++){
      if (number[i] != 0)
        num_casting = number[i] - '0';
    }
    if(num_casting == 0 && strlen(number) == 1)printf("1\n");
    else if (num_casting == 1 && strlen(number) == 1)printf("66\n");
    else{
      switch (num_casting) {
        case 1: printf("16\n"); break;
        case 2: printf("56\n"); break;
        case 3: printf("96\n"); break;
        case 4: printf("36\n"); break;
        case 5: printf("76\n"); break;
        case 6: printf("16\n"); break;
        case 7: printf("56\n"); break;
        case 8: printf("96\n"); break;
        case 9: printf("36\n"); break;
        case 0: printf("76\n"); break;

      }
    }
  }

  return 0;
}
