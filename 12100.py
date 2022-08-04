#Juan Esteban Floyd J
#solucion al problema 12100 judge online(https://onlinejudge.org/external/121/12100.pdf)
from sys import stdin

def solucion(dic, parejas, elementoBuscar):
	tiempo = 0
	flag = True
	k = 0
	while (flag):
		aux = None #se crea la variable
		if (parejas[k][0] == dic[-1][0]): #parejas es la cola con su pos, como dic esta ordenado, puedo asegurar que el que esta en la ultima pos, es del de mayor prioridad
			dic[-1][1] -= 1 #si esta en la ultima pos, le debe restar uno a las repeticiones de ese elemento
			if (dic[-1][1] == 0):
				dic.pop() #si sus repticiones es igual a 0, debe eliminarlo
			tiempo += 1 #aumenta el tiempo
			aux = parejas.pop(k) #ultima pareja, es decir,elemento con mas proridad actual
			if (k >= len(parejas)): #si el k supera el len de parejas
				k = 0 #se restablece
		else:
			k = ((k+1) % len(parejas)) #forma de iterar sin que se salga del rango
		if (aux == elementoBuscar):
			flag = False #si el elemento que buscamos es igual al elemento que tengo 

	return tiempo

def main():
	casos = int(stdin.readline())
	for i in range(casos): 
		n, m = map(int, stdin.readline().split())
		cola = list( map(int, stdin.readline().split()) )
		dicPrioridades = dict()
		parejas = []
		for e, p in enumerate(cola): #enumerate, elementos de una lista de cero a uno y genera una pareja, donde esta la e va el numero y la p es el punto primer elemento (0,p)
			parejas.append((p, e)) #pareja de la forma(prioridad, pos de esa prioridad)
			if (dicPrioridades.get(p) == None): #si no esta es prioridad
				dicPrioridades[p] = 1 #la crea con una repeticion
			else: 
				dicPrioridades[p] += 1 #si ya existe le suma uno
		dicPrioridades = [ [k, dicPrioridades[k]] for k in dicPrioridades ] #lista donde cada subLista es la prioridad y su repetecion				
		dicPrioridades.sort()
		print(solucion(dicPrioridades, parejas, parejas[m]))
main()