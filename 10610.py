from sys import stdin
from math import sqrt
from queue import Queue

def segundos(m): return m*60
def distancia(p1, p2): return sqrt( (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 )
def metros(v, t): return v*t

def solucion(d, sp, puntos, distP):
    qp = Queue()
    for i in range(len(puntos)):
        if distancia(sp, puntos[i]) <= d:
            qp.put(i)
            distP[i] = 1

    while (not qp.empty()):
        p = qp.get()
        for i in range(len(puntos)):
            if distancia(puntos[p], puntos[i]) <= d and distP[i] > distP[p] + 1:
                if (distP[i] == float('inf')):
                    qp.put(i)
                distP[i] = distP[p] + 1

def main():
    v, m = 0, 0
    v, m = map(int, stdin.readline().strip().split())
    while (v or m):
        m = segundos(m)
        d = metros(v, m)
        sp = tuple(map(float, stdin.readline().strip().split()))
        tp = tuple(map(float, stdin.readline().strip().split()))
        puntos, distP = [], []
        tmp = stdin.readline()
        while (tmp != '\n'):
            puntos.append( tuple(map(float, tmp.strip().split()) ))
            distP.append(float('inf'))
            tmp = stdin.readline()
        puntos.append(tp)
        distP.append(float('inf'))
        solucion(d, sp, puntos, distP)
        print('Yes, visiting {0} other holes.'.format(distP[-1] - 1) if distP[-1] != float('inf') else 'No.')
        v, m = map(int, stdin.readline().strip().split())

main()