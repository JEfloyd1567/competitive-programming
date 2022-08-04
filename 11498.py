from sys import stdin
def main():
	while(True):
		k=int(input())
		if(k == 0):
			break
		else:
			n,m=map(int,stdin.readline().strip().split())
			for i in range(k):
				x,y=map(int,stdin.readline().strip().split())
				if(x>n and y>m):
					print("NE")
				elif(x<n and y>m):
					print("NO")
				elif(x<n and y<m):
					print("SO")
				elif(x>n and y<m):
					print("SE")
				elif(x==n or y==m):
					print("divisa")
main()