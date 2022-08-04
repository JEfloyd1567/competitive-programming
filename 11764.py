from sys import stdin

def main():
	casos=int(input())
	for i in range(casos):
		bajos=0
		altos=0
		paredes=int(input())
		listaParedes=list(map(int,stdin.readline().strip().split()))
		k=1
		while(k<len(listaParedes)):
			p=k-1
			if(listaParedes[k]<listaParedes[p]):
				bajos += 1
			elif(listaParedes[k]>listaParedes[p]):
				altos += 1
			k += 1
		print("Case "+str(i+1)+":",altos,bajos)
	
main()