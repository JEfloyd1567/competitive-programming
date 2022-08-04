from sys import stdin
    
def dfsAux(v):
    global contador,visitado,G 
    if not visitado[v]:
        contador += 1
    visitado[v] = 1
    for u in G[v]:
        if visitado[u]==0:
            dfsAux(u)


def main():
    global contador,visitado,G
    casos = int(stdin.readline())
    for i in range(casos):
        contador = 0
        n,m,l = list(map(int, stdin.readline().split()))
        G=[[] for _ in range(n+1)]
        visitado=[0 for i in range(n+1)]
        for k in range(m):
            n1,n2 =list(map(int, stdin.readline().split()))
            G[n1].append(n2)
        for p in range(l):
            dfsLine=int(stdin.readline())
            dfsAux(dfsLine)
        print(contador)
        contador=0
        G=[[] for _ in range(n+1)]
        visitado=[0 for i in range(n+1)]

main()
