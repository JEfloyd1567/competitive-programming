from sys import stdin

def main():
	cant=0
	casos=int(input())
	for i in range(casos):
		line=list(map(str,stdin.readline().strip().split()))
		accion=line[0]
		if(accion=="donate"):
			dinero=int(line[1])
			cant=cant+dinero
		else:
			print(cant)		
main()