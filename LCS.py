from sys import stdin

"""
Subsecuencia comun mas larga (longest Common Subsequence(LCS))
programacion dinamica
"""

def lcs(n, m, A, B):
	ans = None
	if n == 0 or m == 0:
		ans = 0
	elif(A[n - 1] == B[m - 1]):
		ans = 1 + lcs(n-1, m-1, A, B)
	else:
		ans = max(lcs(n - 1, m, A, B), lcs(n, m-1, A, B))

def lcs_memo(n, m, A, B, mem):
	"""
	lcs abordado desde la programacion dinamica, con memorizacion
	O(N * M)
	N = longitud cadena 1
	M = Longitud cadena 2
	"""
	ans = None
	if( (n, m) in mem ):
		ans = mem[ (n, m) ]
	else:
		if n == 0 or m == 0:
			ans = 0
		elif(A[n - 1] == B[m - 1]):
			ans = 1 + lcs_Memo(n-1, m-1, A, B, mem)
		else:
			ans = max(lcs_Memo(n - 1, m, A, B, mem), lcs_Memo(n, m-1, A, B, mem))
		mem[ (n, m) ] = ans

	return ans
		
def lcs_tab(A, B):
	"""
	lcs abordado desde la programacion dinamica, con tabulacion
	complejidad temporal = O( N + 1 * M + 1)
	complejidad espacial = O( N + 1 * M + 1)
	tab[i][j] = lcs(i,j)

	x1 = tab[i][j]
	x4 = tab[i-1][j-1]
	x2 = tab[i-1][j]
	x3 = tab[i][j-1]
	x5 = tab[N][M] -> solucion
	N = Longitud de la cadena 1
	M = Longitus de la cadena 2
	[ [],   [],  []
	 [x4], [x2], []
	 [x3], [x1], []
	 [],   [],   [x5] ]
	"""
	N = len(A)
	m = len(B)
	tab = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
	for n in range(1, N + 1):
		for m in range(1, M + 1):
			if(A[n - 1] == B[m - 1]):
				tab[n][m] = 1 + tab[n - 1][m - 1]
			else:
				tab[n][m] = max(tab[n - 1][m], tab[n][m - 1])
	return tab[N][M]



def lcs_tab_opt(A, B):
		"""
	lcs abordado desde la programacion dinamica, con tabulacion
	complejidad temporal = O( N + 1 * M + 1)
	complejidad espacial = O(M)
	tab[i][j] = lcs(i,j)

	x1 = tab[i][j]
	x4 = tab[i-1][j-1]
	x2 = tab[i-1][j]
	x3 = tab[i][j-1]
	x5 = tab[N][M] -> solucion
	N = Longitud de la cadena 1
	M = Longitus de la cadena 2
	[ [],   [],  []
	 [x4], [x2], []
	 [x3], [x1], []
	 [],   [],   [x5] ]
	"""
	N = len(A)
	m = len(B)
	prev, new = [0 for _ in range(M + 1)], [None for _ in range(N + 1)]
	for n in range(1, N + 1):
		for m in range(1, M + 1):
			if(A[n - 1] == B[m - 1]):
				new[m] = 1 + prev[m - 1]
			else:
				new[m] = max(prev[m], new[m - 1])
	prev = list(new)
	return prev[M]






