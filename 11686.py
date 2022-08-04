from sys import stdin 
from collections import deque


def khan(G):
	global topo, cola, n, vis
	vis = 0
	topo=[]
	cola = deque()
	for i in range(n):
		if inc[i] == 0:
			cola.append(i)
	while len(cola) != 0:
		v = cola.popleft()
		topo.append(v)
		for i in range(len(G[v])):
			u = G[v][i]
			inc[u] -= 1
			if inc[u] == 0:
				cola.append(u)
		vis += 1
	if vis != n:
		print("IMPOSSIBLE")
	else:
		for i in range(n):
			print(topo[i]+1)

def main():
	global G, n, inc, adj, topo, a ,b
	n, m = list(map(int, stdin.readline().split()))
	while(n != 0):
		inc=[0 for i in range(n)]
		G=[[] for _ in range(n)]
		for i in range(m):
			a, b = list(map(int,stdin.readline().split()))
			G[a-1].append(b-1)
			inc[b-1] += 1
		khan(G)
		n, m = list(map(int, stdin.readline().split()))


main()