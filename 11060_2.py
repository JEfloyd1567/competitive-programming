from sys import stdin
from heapq import heappush, heappop

def incidencia(grafo, dic):
    ans, ans2 = [0]*len(dic), []
    tmp = [[] for _ in range(len(dic))]
    for x, y in grafo:
        ans[dic[y]] += 1
        tmp[dic[x]].append(dic[y])
    for i in range(len(ans)):
        if (ans[i] == 0):
            heappush(ans2, i)
    return ans, ans2, tmp

def solucion(cp, incidencia2, grafo, dic):
    ans = []
    while len(cp):
        ans.append(heappop(cp))
        incidencia2[ans[-1]] = -1
        for u in grafo[ans[-1]]:
            incidencia2[u] -= 1
            if (incidencia2[u] == 0):
                heappush(cp, u)

    ans = [ dic[u] for u in ans ]
    return ans

def main():
    lines = stdin.readlines()
    lines.reverse()
    case = 1
    while len(lines):
        n = int(lines.pop())
        names = [ lines.pop().strip() for _ in range(n) ]
        dic = { n:e for e, n in enumerate(names) }
        dicR = { e:n for e, n in enumerate(names) }
        m = int(lines.pop())
        grafo = [ lines.pop().strip().split() for _ in range(m) ]
        incidencia3, cp, grafo = incidencia(grafo, dic)
        print('Case #{0}: Dilbert should drink beverages in this order: {1}.\n'.format(case, ' '.join(solucion(cp, incidencia3, grafo, dicR))))
        case += 1
        if (len(lines)): 
            lines.pop()
    
    return 0

main()