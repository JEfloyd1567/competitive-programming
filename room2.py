from sys import stdin

def act(A, N, n, t):
	A.sort(key = lambda x: x[1])
	ans = None
	if n==N:
		ans = 0
	else:
		if A[n][0]<t: 
			ans = act(A, N, n+1, t)
		else:
			ans = 1 + act(A, N, n+1, A[n][1])
	return ans



def main():
	n = int(stdin.readline())
	for i in range(n):
		l = []
		s,f = map(int, stdin.readline().strip().split())
		while(f != 0):
			l.append((s,f))
			s,f = map(int, stdin.readline().strip().split())
		ans = act(l,len(l),0,0)
		print(ans)
main()