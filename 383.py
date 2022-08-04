#solucion al problema 383 de judge online(https://onlinejudge.org/external/3/383.pdf)
#Juan Esteban Floyd Jimenez
#bfs basado al de la pagina: https://www.cramirez.info/teaching/agra/2021-2

from sys import stdin
from collections import deque

def bfsAux(salida):
    global visitados,G,nivel
    cola = deque()
    cola.append(salida)
    visitados[salida] = True
    while len(cola) != 0:
        v = cola.popleft()
        for i in range(len(G[v])):
            k = G[v][i]
            if not visitados[k]:
                cola.append(k)
                nivel[k]=nivel[v]+ 1
                visitados[k] = True


def main():
    global G,visitados,contador,nivel
    conjunto=int(input())
    print("SHIPPING ROUTES OUTPUT")
    for i in range(conjunto):
        print("\nDATA SET  "+str(i+1)+"\n")
        m,n,p=list(map(int,stdin.readline().split()))
        G=[[] for _ in range(m+1)] 
        nivel=[0 for _ in range(m+1)]
        visitados=[False for _ in range(m+1)]
        diccionario={}
        nombres=list(map(str,stdin.readline().split()))
        for d in range(len(nombres)):
            diccionario[nombres[d]]=d
        for k in range(n):
            conexiones=list(map(str,stdin.readline().split()))
            clave=diccionario[conexiones[0]]
            clave2=diccionario[conexiones[1]]
            G[clave2].append(clave)
            G[clave].append(clave2)
        for t in range(p):
            numero,salida,destino=list(map(str,stdin.readline().split()))
            clave=diccionario[salida]
            clave2=diccionario[destino]
            costo=int(numero)*100
            visitados=[False for _ in range(m+1)]
            nivel=[0 for _ in range(m+1)]
            bfsAux(clave)
            aux=diccionario[destino]
            if(nivel[aux] == 0):
                print("NO SHIPMENT POSSIBLE")
            else:
                print("$"+str((costo)*nivel[aux]))
        G=[[] for _ in range(m+1)] 
    print("\nEND OF OUTPUT")
main()