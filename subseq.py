'''
generacion de subsequencias
'''
sols = []

def phi(A, N, n, B):
	'''
	complejidad temporal = O(n*2^n)
	comlejidad espacial = O(n)
	'''
	if(n == N):
		print(B)
	else:
		phi(A, N, n + 1, B)
		B.append(A[n])
		phi(A, N, n + 1, B)
		B.pop()




