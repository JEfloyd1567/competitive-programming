#include <iostream>
#include <math.h>

using namespace std;

double radianes(double grados) { return grados*M_PI/180; }
double f(double L1, double a, double L) { return ((2*L1*sin(a/2.)) / a) - L;}
double d(double R, double L) { return R - sqrt( R*R - (L*L)/4 ); }
double R(double a, double L) { return L/a; }
double Lprima(double L, double n, double C) { return (1 + n*C)*L; }

double binarySearch(double low, double hi, double L, double L1, int times) {
    double ans = (low + hi) / 2.0;
    if (low != hi && times) {
        if (f(L1, radianes(ans), L) >= 0) { ans = binarySearch(ans, hi, L, L1, times - 1); }
        else { ans = binarySearch(low, ans, L, L1, times - 1); }
    }
    return ans;
}

double resolver(double L, double L1) {
    double ans, angulo;
    angulo = radianes(binarySearch(0, 180, L, L1, 200));
    ans = d(R(angulo, L1), L);
    return ans;
}

int main() {
    double L, n, C, L1;
    cin >> L >> n >> C;
    while ( L >= 0 && n >= 0 && C >= 0 ) {
        L1 = Lprima(L, n, C);
        if (L1 == L) { printf("%.3f\n", 0.); }
        else { printf("%.3f\n", resolver(L, L1)); }

        cin >> L >> n >> C;
    }
    return 0;
}

