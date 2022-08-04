from sys import stdin

"""
Subsecuencia comun mas larga (longest Common Subsequence(LCS))
programacion dinamica
"""
dic = {}

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
			ans = 1 + lcs_memo(n-1, m-1, A, B, mem)
		else:
			ans = max(lcs_memo(n - 1, m, A, B, mem), lcs_memo(n, m-1, A, B, mem))
		mem[ (n, m) ] = ans

	return ans
		

def main():
	line = stdin.readline().strip().split()
	line2 = stdin.readline().strip().split()
	while( line != ''):
		print(lcs_memo(len(line[0]),len(line2[0]),line[0], line2[0], dic))
		line = stdin.readline().strip().split()
		line2 = stdin.readline().strip().split()

main()

