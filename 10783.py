from sys import stdin

def main():
	t=int(stdin.readline())
	for i in range(t):
		a=int(stdin.readline())
		b=int(stdin.readline())
		k=int(a)
		suma = 0
		while(k <= b):
			if((k % 2) != 0):
				suma = suma + k
			k += 1
		print("Case "+ str(i+1)+": "+str(suma))
main()