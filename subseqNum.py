'''
Considere un arreglo A[0..N), N ≥ 0, que representa un conjunto de números y no tiene elementos repetidos. El
objetivo es diseñar un algoritmo que enumere todas las subsecuencias de A.
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

A=[i for i in range(10)]
phi(A, len(A), 0, [])


