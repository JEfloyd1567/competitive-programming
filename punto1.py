from sys import stdin

def sel_act_greedy(A):
	"""
	complejidad temporal, porque hay que ordenar O(nlog(n)), si ya estuviera ordenado seria: O(n)
	complejidad espacial, retornando la cantidad O(1), retornando los elementos O(n)
	"""
	A.sort(key = lambda x: x[1])
	ans = 0
	lans = []
	N = len(A)
	n = 0
	while(n < N):
		best = n
		lans.append(best) 
		ans += 1
		n += 1
		while((n < N) and (A[n][0] < A[best][1])):
			n += 1
	return ans,lans



def main():
	n = int(stdin.readline())
	for i in range(n):
		l = []
		s,f = map(int, stdin.readline().strip().split())
		while(f != 0):
			l.append((s,f))
			s,f = map(int, stdin.readline().strip().split())
		ans,l2 = sel_act_greedy(l)
		print(ans)
main()