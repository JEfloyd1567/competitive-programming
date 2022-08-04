#include <iostream>
#include <stdio.h>
#include <string>
#include <map>
#include <queue>
#include <set>
#include <iterator>
#include <algorithm>

using namespace std;

int main(){
  int Q, period, k;
  string action;
  map<int, int> reg;
  pair<int, int> p;
  priority_queue <pair<int, int>, vector< pair<int, int> >, greater<pair<int, int>>> pq;

  while(true){
    cin >> action;
    //Leyendo si la primera palabra es un "Register" o un "#"

    if(action == "#"){
      //Si es un "#" entonces se deja de leer
      break;
    }else{
      //Si es un "Register" entonces se leen el número Q y el periodo
      cin >> Q >> period;

      reg[Q] = period;
      //En el registro se asignan que para el número Q le corresponde el periodo period

      pq.push( {period, Q} );
      //Se agregan a la cola de prioridad el periodo y el número Q
    }
  }

  cin >> k;
  //Dado que action sea igual a "#" entonces se termina el ciclo infinito y se lee el número k

  while(k--){
    //Se itera k veces en este ciclo

    p = pq.top();
    // p es el tope de la cola de prioridad

    pq.pop();
    //Se elimina ese tope

    cout << p.second << endl;
    //Se imprime el número Q

    p.first += reg[p.second];
    //Aquí lo que se hace es sumarle al periodo que ya llevaba el registro de Q, en este caso p.second es el número Q del tope de la cola de prioridad
    
    pq.push(p);
    //Se agrega a la cola de prioridad la pareja {period, Q} en donde podemos ver que a period en la línea anterior se le sumó el registro de Q
  }

  return 0;
}
