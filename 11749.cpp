//solucion al problema 11749 de judge online (https://onlinejudge.org/external/117/11749.pdf)
//Juan esteban Floyd Jimenez
//dfs basado al de la pagina: https://www.cramirez.info/teaching/agra/2021-2

#include <iostream>
#include <cstdio>
#include <vector>
#include <climits>
#include <algorithm>

using namespace std;

int contador;

void dfsAux(int v, vector< vector<int> > &G, vector< vector<int> > &W, int pesoMax, vector <int> &visitado){
    int u, i, aux;
    visitado[v] = 1;
    for(i = 0; i < G[v].size(); i++){
        int nodo = G[v][i];
        int aux = W[v][i];
        if(visitado[nodo] == 0 && aux==pesoMax){
            contador++;
        	dfsAux(nodo, G, W, pesoMax, visitado);
        }
    }	
}

int max(vector<int> &arr){
    int maximo = INT_MIN;
    for(int i = 0; i<arr.size() ; i++){
        if( maximo < arr[i]){
            maximo = arr[i];
        }
    }
    return maximo;
}

int main(){
	int n, m, n1, n2, ppa, pesoMax, aux2;
    scanf("%d %d", &n, &m);
	while(n!=0 || m!=0){
        pesoMax = INT_MIN; 
		vector< vector<int> > G(n);
		vector< int > visitado(n,0);
		vector< vector<int> > W(n);
        for(int i=0; i<m ; i++){
            scanf("%d %d %d", &n1, &n2, &ppa);
            if(pesoMax < ppa){
                pesoMax = ppa;
            }
            G[n1-1].push_back(n2-1);
            G[n2-1].push_back(n1-1);
            W[n1-1].push_back(ppa);
            W[n2-1].push_back(ppa);
        }
        vector<int>arr;
        for (int k = 0 ; k<n ; k++){
            contador = 1;
            dfsAux(k, G, W, pesoMax, visitado);
            aux2=contador;
            arr.push_back(aux2);
        }
        printf("%d\n", max(arr) );
        scanf("%d %d", &n,&m);
	}
}