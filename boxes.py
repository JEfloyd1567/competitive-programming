from sys import stdin
"""
boxes.py
"""

A=[]
N , B = None, None

def ok(tam):
	b , n = 0, 0
	while(b <= B and n != N):
		bc  = A[n] // tam 
		red = A[n] % tam
		if(red != 0):
			bc += 1
		b, n = b + bc, n + 1
	return b <= B 

def solve():
	low = 0 
	hi = max(A)
	while(low + 1 != hi): 
		mid = low + ((hi - low ) >> 1)
		if( ok(mid) ):
			hi = mid
		else:
			low = mid
	return hi

def main():
	global A, N, B
	N,B = map(int, stdin.readline().split())
	while(N != -1):
		A = [ int(stdin.readline()) for _ in range(N) ]
		stdin.readline()
		print(solve())
		N,B = map(int, stdin.readline().split())
main()

