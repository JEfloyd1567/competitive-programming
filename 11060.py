from sys import stdin
from heapq import heappush, heappop

def degree(graph, dic):
    ans, ans2 = [0]*len(dic), []
    tmp = [[] for _ in range(len(dic))]
    for x, y in graph:
        ans[dic[y]] += 1
        tmp[dic[x]].append(dic[y])
    for i in range(len(ans)):
        if (ans[i] == 0):
            heappush(ans2, i)
    return ans, ans2, tmp

def solve(heap, incidence, graph, dic):
    ans = []
    while len(heap):
        ans.append(heappop(heap))
        incidence[ans[-1]] = -1
        for u in graph[ans[-1]]:
            incidence[u] -= 1
            if (incidence[u] == 0):
                heappush(heap, u)

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
        graph = [ lines.pop().strip().split() for _ in range(m) ]
        incidence, heap, graph = degree(graph, dic)
        print('Case #{0}: Dilbert should drink beverages in this order: {1}.\n'.format(case, ' '.join(solve(heap, incidence, graph, dicR))))
        case += 1
        if (len(lines)): 
            lines.pop()
    
    return 0

main()