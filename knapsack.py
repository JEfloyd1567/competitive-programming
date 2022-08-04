def knapsack(n, m, W, B):
	"""
	O(n*n^2)
	"""
	if(n == 0 or m == 0):
		ans = 0
	elif(W[n - 1] <= m):
		ans = max(knapsack(n - 1, m - W[n - 1], W, B) + B[n - 1], knapsack(n - 1, m, W, B))
	else:
		ans = knapsack(n - 1, m, W, B)
	return ans

def knapsack_memo(n, m, W, B, mem):
	"""
	O(N * M)
	"""
	if((n, m) in mem):
		ans = mem[(n, m)]
	else:
		if(n == 0 or m == 0):
			ans = 0
		elif(W[n - 1] <= m):
			ans = max(knapsack_memo(n - 1, m - W[n - 1], W, B, mem) + B[n - 1], knapsack_memo(n - 1, m, W, B, mem))
		else:
			ans = knapsack_memo(n - 1, m, W, B, mem)
		mem[(n, m)] = ans
	return ans

def knapsack_tab(M, W, B):
	N = len(W)
	tab= [ [0 for _ in range(M + 1)] for _ in range(N + 1)]
	n = 1
	while( n != N):
		m = 1
		while(m != M):
			if(W[n - 1] <= m):
				tab[n][m] = max(tab[n - 1][m - W[n - 1]] + B[n - 1], tab[n - 1][m])
			else:
				tab[n][m] = tab[n - 1][m]
			m += 1
		n += 1
	return tab[N][M]

def knapsack_tab_opt(M, W, B):
	N = len(W)
	prev, curr = [0 for _ in range(M + 1)],  [0 for _ in range(N + 1)]
	n = 1
	while( n != N):
		m = 1
		while(m != M):
			if(W[n - 1] <= m):
				curr[m] = max(prev[m - W[n - 1]] + B[n - 1], prev[m])
			else:
				curr[m] = prev[m]
			m += 1
		prev = list(curr)
		n += 1
	return curr[M]



