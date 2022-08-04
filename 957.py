#Juan Esteban Floyd J
#solucion al problema 957 judge online(https://onlinejudge.org/external/9/957.pdf)

from sys import stdin

def binsearch(A, x, low, hi):
	ans = None
	if low == hi: ans = False
	elif low + 1 == hi: ans = low
	else:
		mid = low + ((hi - low) >> 1) # mid = (low+hi)//2
		if A[mid] <= x: ans = binsearch(A, x, mid, hi)
		else: ans = binsearch(A, x, low, mid)
	return ans

def solucionAux(N, up, papas):
	"""
	esta funcion retorna la solucion para el periodo n
	"""
	ans = []
	pos = binsearch(papas, up, N, len(papas)) #pos del ultimo papa en el periodo n
	ans = [pos - N + 1, papas[N], papas[pos]] #lista de la forma [#papas en periodo, inicio de periodo, anio culminacion del ultimo papa en ese periodo]
	return ans

def solucion(y, papas):
	ans = [ 0, ' ', ' ' ]
	for i in range(len(papas)):
		N = i
		up = papas[i] + y - 1
		tmp = solucionAux(N, up, papas)
		if (ans[0] < tmp[0]):
			ans = tmp #si en el periodo almacenado en ans, hay menos papas que en el periodo i, actualizo 

	ans = list( map(str, ans) ) #retorna la lista con la solucion
	return ans


def main():

	lineas = stdin.readlines() #entrega una lista y los guarda en forma de pila
	lineas.reverse() #invierte para poder obtener el orden correcto de los casos
	while (len(lineas) > 0):
		y = int(lineas.pop()) #obtiene el periodo y
		n = int(lineas.pop()) #obtiene el inicio de periodo N
		papas = [ int(lineas.pop()) for _ in range(n) ] #guarda los n enteros del arreglo lineas y almacenarlos en la lista popes
		print(' '.join(solucion(y, papas)))
		if (len(lineas) > 0):
			lineas.pop()

main()