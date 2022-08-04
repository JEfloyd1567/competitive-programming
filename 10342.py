#posible solucion al problema 10342 judge online (https://onlinejudge.org/external/103/10342.pdf)
#Juan Esteban floyd
#implementacion de dijkstra basada en la de la pagina: https://www.cramirez.info/teaching/agra/2021-2

from sys import stdin
from heapq import heappop, heappush
import math
INF = float('inf') # math.inf

def dijkstra(Gr, s):
	global G,d,visitado,p
	d, p = [[INF,INF] for i in range(len(Gr))], [-1 for i in range(len(Gr))]
	#d[s][0] = 0
	heap = [(0, s)]
	while len(heap) != 0:
		#print('heap:', heap)
		costo, u = heappop(heap)
		if(costo < d[u][0]):
			d[u][0]=costo
		elif(costo < d[u][1]):
			d[u][1] = costo
		#if costo == d[u][0]:
		#print('d:', d)
		for v, w in G[u]:
			if(d[v][1] > d[u][1] + w):
				heappush(heap, (d[u][1]+ w, v))
#			elif d[v][0] > d[u][1] + w:
				#d[v], p[v] = d[u] + w, u
#				heappush(heap, (d[u][1]+ w, v))
			elif d[v][0] > d[u][0] + w:
				#d[v], p[v] = d[u] + w, u
				heappush(heap, (d[u][0]+ w, v))
			elif(d[v][1] > d[u][0] + w) and d[v][1] == INF:
				heappush(heap, (d[u][0]+ w, v))
		#print('heap:', heap)
		#print('d:', d)
	#return d, p

def main():
	global G,visitado,d,p
	line = stdin.readline()
	casos = 1
	while(line != ""):
		line=line.strip().split()
		print("Set #"+str(casos))
		n=int(line[0])
		r=int(line[1])
		G = [[] for _ in range(n)]
		for i in range(r):
			n1,n2,n3 = map(int, stdin.readline().strip().split())
			G[n1].append((n2,n3))
			G[n2].append((n1,n3))
		q = int(stdin.readline())
		for i in range(q):
			origen,destino = map(int, stdin.readline().split())
			dijkstra(G,origen)
			if(d[destino][1] == float("inf")):
				print("?")
			else:
				print(d[destino][1])
		casos += 1
		line = stdin.readline()
		if(line == '\n'):
			line = stdin.readline()
main()