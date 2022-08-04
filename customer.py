from sys import stdin
from heapq import heappush, heappop


def solve(A):
	A.sort(key = lambda x: x[1])
	t = 0
	lans=[]
	aux = None
	for i in range(len(A)):
		#print('lans',lans)
		aux = A[i][0] 
		if((t + aux) <= A[i][1]):
			t += A[i][0]
			heappush(lans,(A[i][0]) * - 1 )

		elif(len(lans) > 0):
			maximo = heappop(lans)
			if(aux < (maximo * - 1)):
				t -= maximo * - 1
				t += aux
				heappush(lans,(A[i][0]) * -1 )
			else:
				heappush(lans,maximo)
	return len(lans)

def main():
	casos = int(stdin.readline())
	for i in range(casos):
		lineEnBlanco = stdin.readline()
		n = int(stdin.readline())
		l=[]
		for k in range(n):
			q,d = map(int,stdin.readline().strip().split())
			l.append((q,d))
		print(solve(l))
		if(i < casos - 1):
			print()
main()