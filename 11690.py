#posible solucion al problema, funciona con casos del pdf y udebug 11690 de judge online (https://onlinejudge.org/external/116/11690.pdf)
#Juan esteban Floyd Jimenez
#dfs basado al de la pagina: https://www.cramirez.info/teaching/agra/2021-2

from sys import stdin
import sys

sys.setrecursionlimit(9000)

def dfsAux(v):
	global G, visitado, dinero, o, aux, n
	visitado[v] = 1
	aux += dinero[v]
	for u in G[v]:
		if visitado[u] == 0:
			dfsAux(u)


def main():
	global G, visitado, dinero, o, aux, n 
	N = int(stdin.readline())
	for i in range(N):
		n,m = map(int, stdin.readline().split())
		G = [ [] for _ in range(n) ]
		visitado = [ 0 for _ in range(n)]
		dinero = []
		for k in range(n):
			o = int(stdin.readline())
			dinero.append(o)
		for p in range(m):
			x,y = map(int, stdin.readline().split())
			G[x].append(y)
			G[y].append(x)
		aux = 0
		dfsAux(0)
		posible=False
		imposible=False
		if(aux == 0):
			for h in range(len(visitado)):
				if(visitado[h] == 0):
					dfsAux(h)
					if(aux == 0):
						posible=True
					else:
						imposible=True
		else:
			imposible=True
		if(aux == 0):
			posible=True

		if(posible):
			print("POSSIBLE")
		else:
			print("IMPOSSIBLE")

main()