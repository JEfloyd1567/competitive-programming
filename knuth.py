from sys import stdin


def knuths(A, N, n, B):
	if(len(B) == N):
		print(''.join(B))
	else:
		for i in range(len(B) + 1):
			B.insert(i,A[n])
			knuths(A, N, n + 1, list(B))
			del B[i]

def main():
	lines = stdin.readlines()
	for i in range(len(lines)):
		arr=list(lines[i].strip())
		knuths(arr, len(arr), 0, [])
		if(i + 1 < len(lines)):
			print()
main()