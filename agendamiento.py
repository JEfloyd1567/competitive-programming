def sel_act_greedy(A):
	"""
	complejidad temporal, porque hay que ordenar O(nlog(n)), si ya estuviera ordenado seria: O(n)
	complejidad espacial, retornando la cantidad O(1), retornando los elementos O(n)
	"""
	A.sort(key = lambda x: x[1])
	print(A)
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
	A=[(0,6),(5,7),(8,9),(5,9),(1,2),(3,4),(0,5)]
	print(sel_act_greedy(A))
main()