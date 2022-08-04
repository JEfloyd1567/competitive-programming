//aproximacion a una solucion del problema 11561 de online judge, funciona con los casos del pdf y de udebug
// Juan Esteban Floyd Jimenez

#include <iostream>
#include <cstdio>
#include <vector>
#include <queue>

using namespace std;

string movimientos[4] = {"NORTE", "SUR", "OESTE", "ESTE"}; //movimientos posibles

int* moverse(string accion, int *pos) {
//movimientos posibles en el tablero de juego
	int *ans = new int[2];
	ans[0] = pos[0];
	ans[1] = pos[1];

	if (accion == "NORTE") {
		ans[0]++;
	}
	else if (accion == "SUR") {
		ans[0]--;
	}
	else if (accion == "OESTE") {
		ans[1]--;
	}
	else {
		ans[1]++;
	}

	return ans;
}

bool esValido(vector<string> tablero, int *pos) {
//verfica si hay una posicion valida o no la hay
	bool ans = true;

	if (tablero[pos[0]][pos[1]] == '#' || tablero[pos[0]][pos[1]] == 'T') {
		ans = false; //si no es valida, retorna False
	}
	else {

		for (int i = 0; i < 4; i++) {
			int *npos = moverse(movimientos[i], pos);
			ans = ans && !(tablero[npos[0]][npos[1]] == 'T'); //de lo contrario, ans se actualiza una posicion nueva, si no es una trampa
		}
	}

	return ans;
}


int bfsTablero(vector<string> tablero, int *pos, int ancho, int largo) {
//bfs adaptado para el tablero del juego
	int ans = 0;
	queue< int* > frontier;
	int visitados[largo][ancho]; //matriz de visitados
	frontier.push(pos);
	int *npos;
	while ( !frontier.empty() ) {

		npos = frontier.front(); 
		frontier.pop();
	
		if (esValido(tablero, npos) && visitados[npos[0]][npos[1]] != 1) {

			visitados[npos[0]][npos[1]] = 1; //si su posicion es valida se agrega a visitados

			for (int i = 0; i < 4; i++) {

				int *aux = moverse(movimientos[i], npos); 
				
				if (visitados[aux[0]][aux[1]] != 1) {
					
					if ( visitados[aux[0]][aux[1]] != 2 && tablero[aux[0]][aux[1]] == 'G') {
						ans++; //si es una pieza de oro, aumenta el contador
					}
					frontier.push(aux);
					visitados[aux[0]][aux[1]] = 2;
				}

			}

		}
	}

	return ans;
}


int solucion(vector<string> tablero, int *pos, int ancho, int largo) {

//se lanza bfs desde el nodo que se indique
	int ans = 0;

	ans = bfsTablero(tablero, pos, ancho, largo);

	return ans;
}

int main() {

	int ancho, largo;

	while (scanf("%d %d", &ancho, &largo) != EOF) {

		vector<string> tablero;
		string aux;
		int pos[2] = {0, 0};

		for ( int i = 0; i < largo; i++ ) {
			cin >> aux;
			for ( int j = 0; j < ancho; j++ ) {
				if ( aux[j] == 'P' ) {
					//si es igual a "P" se guarda esa posicion
					pos[0] = i;
					pos[1] = j;
				}
			}
			tablero.push_back(aux); //se crea el mapa
		}
		//se lanza solucion con el mapa, la posicion de "P", ancho y largo
		cout << solucion(tablero, pos, ancho, largo)<<endl;
	}
	return 0;
}	