#include <stdio.h>
#include <string.h>

int max(int B[], int color[]){
  int i,j,ans=-1;
  for (j=0;j<3;j++)
    if (B[j]>ans && color[j]==-1){i=j;ans=B[j];}
  return i;
}

int solve(int A[][3]){
  int i,j,k,ans = 0;
  // 0:B ; 1:G ; 2:C
  char bin[3];
  int color[3] = {-1,-1,-1};
  for(j=0;j<3;j++){
    int B[3] = {A[0][j],A[1][j],A[2][j]};
    i = max(B,color);
    for(k=0;k<3;k++)
      if(k!=i){ans = ans + A[k][j];}
    switch (j){
      case 0:
        bin[i] = 'B';
        break;
      case 1:
        bin[i] = 'C';
        break;
      case 2:
        bin[i] = 'G';
        break;
    }
    color[i] = 1;
  }
  printf("%s %d\n", bin,ans);
  return ans;
}

int main(){ 

  int a[9];
  while(scanf("%d %d %d %d %d %d %d %d %d",&a[0],&a[1],&a[2],&a[3],
    &a[4],&a[5],&a[6],&a[7],&a[8])!=EOF){
    int A[3][3] = {
      {a[0],a[1],a[2]},
      {a[3],a[4],a[5]},
      {a[6],a[7],a[8]}
    };
    solve(A);
  }
  return 0;
}