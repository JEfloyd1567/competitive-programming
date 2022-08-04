from sys import stdin
def main():
	casos=int(input())
	for i in range(casos):
		mayor=0
		menor = 0
		numero=int(input())
		arr=list(map(int,stdin.readline().strip().split()))
		mayor=max(arr)
		menor=min(arr)
		distancia=(mayor-menor)*2
		print(distancia)
main()