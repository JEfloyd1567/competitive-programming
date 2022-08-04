#solucion al problema 12376 de judge online (https://onlinejudge.org/external/123/12376.pdf)
#Juan esteban Floyd Jimenez
#dfs basado al de la pagina: https://www.cramirez.info/teaching/agra/2021-2

from sys import stdin

def dfsAux(v):
    global G, visitado, contador, sgtnodo
    visitado[v] = 1
    contador += listaAprendizaje[v]
    maximo = -1
    for u in G[v]:
        if(listaAprendizaje[u] > maximo):
            maximo = listaAprendizaje[u]
            sgtnodo = u
    if visitado[sgtnodo] == 0:
        dfsAux(sgtnodo)

def main():
    global G, visitado, listaAprendizaje, contador, sgtnodo
    t=int(stdin.readline())
    for i in range(t):
        lineaEnBlanco=stdin.readline()
        n, m = map(int, stdin.readline().split())
        listaAprendizaje=list(map(int, stdin.readline().split()))
        G = [[] for _ in range(n)]
        visitado=[0 for _ in range(n)]
        contador = 0
        sgtnodo=0
        for k in range(m):
            n1,n2 =list(map(int, stdin.readline().split()))
            G[n1].append(n2)
        dfsAux(0)
        print("Case " + str(i+1) + ":" + " " + str(contador) + " " + str(sgtnodo))
main()
