from sys import stdin
#12 74
def main():
	while(True):
		distanciaAB=0
		distanciaBA=0
		a,b=list(map(int,stdin.readline().strip().split()))
		if(a==-1 and b==-1):
			break;
		else:
			copiaA=int(a)
			copiaB= int(b)
			resta=abs(copiaB-copiaA)
			resta2=abs((copiaB+100)-copiaA)
			resta3=abs((copiaA+100)-copiaB)
			print(min(resta,resta2,resta3))
main()