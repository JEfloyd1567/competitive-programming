// Juan Esteban Floyd J
// solucion al problema 11881 de online judge (https://onlinejudge.org/external/118/11881.pdf)
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;

double npv( vector<int> cf, int t, double irr ) {
	//formula del problema

	double ans = 0;

	for ( int i = 0; i < t+1; i++ ) {
		ans += cf[i]/pow(1 + irr, i);
	}

	return ans;
}


double biseccion( double low, double hi, vector< int > cf, int t , int stop) {
// metodo biseccion interativo, debido a que el intervalo de busqueda es infinito, stop es un limite de pasos, se ajusta acorde al valor que se necesite
	double mid;

	while (low <= hi && stop) {

		mid = (low + hi) / 2;

		if (npv(cf, t, mid) > 0) {
			low = mid;
		}
		else {
			hi = mid;
		}
		stop--;
	}
	return mid;
}


double solucion( int t, vector< int > cf ) {
// realiza biseccion de la formula
	double ans = biseccion(-1, 10000, cf, t, 100);
	return ans;
}

int main() {

	int t;

	cin >> t;
	while (t) {
		vector< int > cf;
		int tmp;
		for ( int i = 0; i < t+1; i++ ) {
			cin >> tmp;
			cf.push_back(tmp);
		}

		printf("%.2f\n", solucion(t, cf));
		cin >> t;
	}

	return 0;
}