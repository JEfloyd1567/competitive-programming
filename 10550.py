from sys import stdin 
def main():
	while(True):
		distanciaAB=0
		distanciaBC=0
		distanciaCD=0
		resultado=0
		a,b,c,d=map(int,stdin.readline().strip().split())
		if(a==0 and b==0 and c==0 and d==0):
			break
		else:
			if(a>b):
				distanciaAB=(a-b)*9
			else:
				distanciaAB=(a+40-b)*9
			if(c>b):
				distanciaBC=(c-b)*9
			else:
				distanciaBC=(c+40-b)*9
			if(c>d):
				distanciaCD=(c-d)*9
			else:
				distanciaCD=(c+40-d)*9
			resultado=1080+distanciaAB+distanciaBC+distanciaCD
			print(resultado)
main()