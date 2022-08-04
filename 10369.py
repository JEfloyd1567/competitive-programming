#solucion al problema 10369 judge online (https://onlinejudge.org/external/103/10369.pdf)
#Juan Esteban floyd
#implementacion de conjuntos disjuntos basada en la de la pagina: https://www.cramirez.info/teaching/agra/2021-2
from sys import stdin
import math

p, rango = [0 for _ in range(501)], [0 for _ in range(501)]

def makeSet(v):
    p[v], rango[v] = v, 0

def findSet(v):
    ans = None
    if v == p[v]: ans = v
    else:
        p[v] = findSet(p[v])
        ans = p[v]
    return ans

def unionSet(u, v):
    u, v = findSet(u), findSet(v)
    if u != v:
        if rango[u] < rango[v]: u, v = v, u
        p[v] = u
        if rango[u] == rango[v]: rango[u] += 1

def solucion(G,s,n):
    ans = None
    limite = n-s
    for i in range(n):
    	makeSet(i)
    G.sort(key=lambda aux: aux[2])
    for l in G:
        u = l[0]
        v = l[1]
        w = l[2]
        if findSet(u) != findSet(v):
            limite -= 1
            ans = w
            unionSet(u,v)
            if limite == 0:
                break
    return ans

def main():
	global G,n,s,listaCoordenadas
	casos = int(stdin.readline())
	for i in range(casos):
		s,p = map(int,stdin.readline().split())
		listaCoordenadas = []
		G = []
		for k in range(p):
			x,y = map(int,stdin.readline().strip().split())
			listaCoordenadas.append((x,y))
		for d in range(p):
			r = d+1
			while(r < p):
				aux = math.sqrt(pow((listaCoordenadas[d][0]-listaCoordenadas[r][0]),2)+pow((listaCoordenadas[d][1]-listaCoordenadas[r][1]),2))
				G.append((d,r,aux))
				r += 1
		numero = solucion(G,s,p)
		print("{:.2f}".format(numero))

main()