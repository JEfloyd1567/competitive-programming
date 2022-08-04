#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

  int b1 = 0, g1 = 0, c1 = 0, b2 = 0, g2 = 0, c2 = 0, b3 = 0, g3 = 0, c3 = 0;
  while (scanf("%d %d %d %d %d %d %d %d %d", &b1, &g1, &c1, &b2, &g2, &c2, &b3, &g3, &c3) != EOF) {

    int brown[3], green[3], clear[3], mov[20];
    char bins[20][4];

    brown[0] = b2 + b3;
    brown[1] = g2 + g3;
    brown[2] = c2 + c3;

    green[0] = b1 + b3;
    green[1] = g1 + g3;
    green[2] = c1 + c3;

    clear[0] = b1 + b2;
    clear[1] = g1 + g2;
    clear[2] = c1 + c2;

    mov[0] = brown[0] + green[1] + clear[2]; strcpy(bins[0], "BGC");
    mov[1] = brown[0] + green[2] + clear[1]; strcpy(bins[1], "BCG");

    mov[2] = brown[1] + green[0] + clear[2]; strcpy(bins[2], "GBC");
    mov[3] = brown[1] + green[2] + clear[0]; strcpy(bins[3], "GCB");

    mov[4] = brown[2] + green[0] + clear[1]; strcpy(bins[4], "CBG");
    mov[5] = brown[2] + green[1] + clear[0]; strcpy(bins[5], "CGB");


    mov[6] = green[0] + brown[1] + clear[2]; strcpy(bins[6], "GBC");
    mov[7] = green[0] + brown[2] + clear[1]; strcpy(bins[7], "CBG");

    mov[8] = green[1] + brown[0] + clear[2]; strcpy(bins[8], "BGC");
    mov[9] = green[1] + brown[2] + clear[0]; strcpy(bins[9], "CGB");

    mov[10] = green[2] + brown[0] + clear[1]; strcpy(bins[10], "BCG");
    mov[11] = green[2] + brown[1] + clear[0]; strcpy(bins[11], "GCB");


    mov[12] = clear[0] + green[1] + brown[2]; strcpy(bins[12], "CGB");
    mov[13] = clear[0] + green[2] + brown[1]; strcpy(bins[13], "GCB");

    mov[14] = clear[1] + green[0] + brown[2]; strcpy(bins[14], "CBG");
    mov[15] = clear[1] + green[2] + brown[0]; strcpy(bins[15], "BCG");

    mov[16] = clear[2] + green[0] + brown[1]; strcpy(bins[16], "GBC");
    mov[17] = clear[2] + green[1] + brown[0]; strcpy(bins[17], "BGC");

    int i, min = mov[0], pos = 0;
    for ( i = 1; i < 18; i++) {

      if (mov[i] < min) {
        min = mov[i];
        pos = i;
      }
      else if (mov[i] == min) {
        if (strcmp(bins[i],bins[pos]) < 0) {
          min = mov[i];
          pos = i;
        }
      }
    }
    printf("%.3s %d\n", bins[pos], min);

  }
  return 0;
}
