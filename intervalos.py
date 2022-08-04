
def min_convering(A, L, H):
	ans = 0
	A.sort()
	N = len(A)
	n = 0
	l = L
	while((n < N) and l < H):
		best = n 
		n = n + 1
		while((n < N) and (A[n][0] <= l)):
			if(A[n][1] > A[best][1]):
				best = n
			n += 1
		l = A[best][1]
		ans += 1
	return ans

def main():
	A=[(7,15),(8,20),(6,8),(4,9),(3,21),(5,22)]
	print(min_convering(A,0,22))
main()