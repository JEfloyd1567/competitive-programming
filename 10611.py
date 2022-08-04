#Juan Esteban Floyd J
#solucion al problema 10611 judge online(https://onlinejudge.org/external/106/10611.pdf)

from sys import stdin 

def binsearch(A, x, low, hi): #busqueda binaria, que me entrega la posicion de A
	ans = None
	if low == hi: ans = False
	elif low + 1 == hi: ans = low
	else:
		mid = low + ((hi - low) >> 1) # mid = (low+hi)//2
		if A[mid] == x: ans = mid
		elif A[mid] < x: ans = binsearch(A, x, mid, hi)
		else: ans = binsearch(A, x, low, mid)
	return ans

def solucion(A, x):
	ans = [None, None]

	pos = binsearch(A, x, 0, len(A))

	low, hi = pos, pos #en la misma pos, encontro o una mayor o menor

	while (low >= 0 and A[low] >= x):
		low -= 1 #encuentra la pos del menor
	while (hi < len(A) and A[hi] <= x):
		hi += 1 #encuentra pos del mayor

	low = 'X' if (low == -1) else A[low] #si el low es negativo es X, sino es el elemento en esa pos
	hi = 'X' if (hi == len(A)) else A[hi] #si hi es igual al len(A) es X, sino es el elemento en esa pos

	ans = [str(low), str(hi)] #arreglo solucion

	return ans

def main():
	N=int(stdin.readline())
	listaMonos=list(map(int, stdin.readline().strip().split()))
	Q=int(stdin.readline())
	listaConsultas=list(map(int,stdin.readline().strip().split()))
	for consulta in listaConsultas:
		print(' '.join(solucion(listaMonos, consulta))) # ''.join quita '' y une por espacios

main()
