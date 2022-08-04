sols = []

def check(sol, n, f):
	ans, i = True, 0
	while(ans and i < n):
		ans = sol[i] != f and sol[i] != f + n - i and sol[i] != f - n + i
		i += 1
	return ans


def queen(A,n):
	global sols
	if n == N:
		sols.append(list(sol))
	else:
		for f in range(N):
			if(check(sol, n, f)):
				sol[n] = f
				queens(sol, n + 1)

