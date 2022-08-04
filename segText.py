def solve(m, A, D):
	'''
	decision
	'''
	if( m == len(A)):
		ans = True
	else:
		k = m + 1 
		ans = True
		while(k <= len(A) and not(ans)):
			if(A[m : k] in D):
				ans = solve(k, A, D) 
			k += 1
	return ans


def solve2(m, sol, A, D):
	'''
	encontrar una solucion
	'''
	if( m == len(A)):
		ans = True
		print(sol)
	else:
		k = m + 1 
		ans = True
		while(k <= len(A) and not(ans)):
			if(A[m : k] in D):
				sol.append(k - 1)
				ans = solve2(k, sol, A, D)
				sol.pop()
			k += 1
	return ans

sols=[]

def solve3(m, sol, A, D):
	'''
	encontrar todas las soluciones
	'''
	global sols
	if( m == len(A)):
		sols.append(list(sol))
	else:
		k = m + 1 
		while(k <= len(A)):
			if(A[m : k] in D):
				sol.append(k - 1)
				ans = solve3(k, sol, A, D)
				sol.pop()
			k += 1


