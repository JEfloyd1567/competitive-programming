from sys import stdin

def main():
	cases=int(input())
	for i in range(cases):
		a,b=map(int,stdin.readline().strip().split())
		if(a>b):
			print(">")
		elif(a<b):
			print("<")
		elif(a == b):
			print("=")
main()