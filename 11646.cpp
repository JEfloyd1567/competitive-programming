// Juan Esteban Floyd J
// solucion al problema 11646 de online judge (https://onlinejudge.org/external/116/11646.pdf)
#include<cmath>
#include<iostream>
#include<cstdio>
using namespace std;

#define eps 1e-8

int main(){
	int casos = 0;
	double a, b;
	while(scanf("%lf : %lf\n",&a, &b) != EOF){
		casos++;
		double low = 0;
		double hi = 200;
		double mid;
		while(hi-low > eps){
			mid = (low + hi) / 2;
			double radio = sqrt(((pow(mid,2))/4) + (pow(b,2)*(pow(mid,2)))/(4*pow(a,2)));
			double angulo = acos(mid / (2 * radio));
			double arco = 2 * radio * angulo;
			if((2 * mid + 2 * arco) > 400){
				hi = mid;
			}
			else{
				low = mid;
			}
		}
		printf("Case %d: %.10lf %.10lf\n",casos, mid, (b * mid)/ a);
	}
}