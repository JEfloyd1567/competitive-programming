from sys import stdin

def main():
	casos = int(stdin.readline().strip())
	for n in range(casos):
		arr=[]
		pos = 0
		cont = 1
		valorBuscar=int(stdin.readline())
		while(valorBuscar >= len(arr)):
			aux = str(cont)
			for n in range(len(aux)):
				arr.append(aux[n])
			pos = pos + 1
			cont = cont + 1
			valorBuscar = valorBuscar - len(arr)
		aux = valorBuscar + len(arr) - 1
		if( aux >= len(arr)):
			aux = aux - len(arr)
			print(arr[aux])
		else:
			print(arr[valorBuscar + len(arr) - 1])
main()