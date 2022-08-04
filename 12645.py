#solucion al problema 12645 judge online (https://onlinejudge.org/external/126/12645.pdf)
#Juan Esteban floyd
#implementacion de toposort basada en la de la pagina: https://www.cramirez.info/teaching/agra/2021-2

from sys import stdin
from collections import deque


def dfs(G, visitado, n):
	l = []
	l.append(n)
	while (len(l) > 0):
		u = l.pop()
		visitado[u] = 1
		for v in G[u]:
			if (visitado[v] == 0):
				l.append(v)

def invertirGrafo(G, nodos):

	G1 = [ [] for _ in range(len(G)) ]
	incidencia = []

	for i in range(len(G)):
		if (i in nodos):
			incidencia.append(0)
		else:
			incidencia.append(-2)

	for i in nodos:
		for u in G[i]:
			if u in nodos:
				G1[u].append(i)
				incidencia[i] += 1

	return G1, incidencia

def toposort(adj, inc, vis):

	n = len(adj)
	topo = []
	cola = deque()
	for i in range(n):
		if inc[i] == 0:
			cola.append(i)
			topo.append(i)

	while len(cola) != 0:
		u = cola.popleft()
		vis[u] = 1
		for i in range(len(adj[u])):
			v = adj[u][i]
			inc[v] -= 1
			if inc[v] == 0:
				cola.append(v)
				topo.append(v)
			vis[v] = 1

	#if vis != n: print("Hay un ciclo")
	#sselse: print(*topo)
	return topo

def solucion(G, incidencia, visitado):

	ans = 0

	dfs(G, visitado, 0)

	incidencia[0] = -1

	l = []
	for i in range(len(incidencia)):

		if (incidencia[i] == 0):
			l.append(i)

	for u in l:
		ans += 1
		dfs(G, visitado, u)

	l = []
	for i in range(len(incidencia)):

		if (visitado[i] == 0):
			l.append(i)

	# for g in G:
	# 	print(g)

	# print("No visitados: ", l)

	G1, incidencia = invertirGrafo(G, l)
	visitado1 = list(visitado)

	# print("Nuevo Grafo")
	# for g in G1:
	# 	print(g)

	# print("No visitados: ", l)
	# print("Incidencia: ", incidencia)

	topo = toposort(G1, incidencia, visitado1)
	# print("Toposort:", topo)
	# print("Visitado1:", visitado1)
	l=[]
	for i in range(len(visitado1)):
		if(visitado1[i] == 0):
			l.append(i)
	# print(l)
	for u in l:
		if (visitado[u] == 0):
			ans += 1
			dfs(G, visitado, u)

	return ans

def main():
	lines = stdin.readlines()
	lines.reverse()
	case = 0
	while (len(lines) > 0):

		n, m = map(int, lines.pop().split())

		incidencia = [ 0 for _ in range(n+1) ]
		visitado = [ 0 for _ in range(n+1) ]
		G = [ [] for _ in range(n+1) ]

		# for g in G:
		# 	print(g)

		for _ in range(m):

			a, b = map(int, lines.pop().split())
			G[a].append(b)

			if (b != 0):
				incidencia[b] += 1

		print(solucion(G, incidencia, visitado))
main()