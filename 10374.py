#Juan Esteban Floyd Jimenez
#solucin al ejercicio 10374 de judge online (https://onlinejudge.org/external/103/10374.pdf)
from sys import stdin

def solucion(val,dic):
    for key, value in dic.items():
         if val == value:
             return key #segun su valor, encuentra la llave en el diccionario

def main():
	casos=int(stdin.readline())
	candidatos={}
	datos={}
	for i in range(casos):
		lineaEnBlanco=stdin.readline() #se debe ignorar esta linea en blanco
		n=int(stdin.readline()) #numero de candidatos y partidos politicos
		for k in range(n):
			candidato=stdin.readline().strip() #lee el nombre del candidato
			partido=stdin.readline().strip() #lee el nombre del partido politico
			candidatos[candidato]= partido #asocia cada candidato con su partido politico en un diccionario
			datos[candidato]=0 #asocia a un cadidayo con su cantidad de votos
		m=int(stdin.readline()) #cantidad de votaciones
		for k in range(m):
			nombre=stdin.readline().strip() #lee el nombre por el cual se va a votar
			if(nombre in candidatos): #si ese candidato, esta inscrito o existe
				datos[nombre] += 1 #se le suma un voto 
		mayor=0
		repeticiones=0
		mayorVotos=max(datos.values()) #encuentra la mayor cantidad de votos
		nombreGanador=solucion(mayorVotos,datos) # encuentra la persona a la que esta asociada esa cantidad de votos
		partidoGanador=candidatos[nombreGanador] #encuentra el partido politico al cual pertence la persona con mayor cantidad votos
		for clave in datos:
			if(datos[clave] == mayorVotos):
				repeticiones += 1 #repticiones me guarda la cantidad de personas con la cantidad maxima de votos
		if(repeticiones > 1):
			print('tie') #si hay mas de una persona con la misma cantidad de votos (cantidad maxima) imprime 'tie'
		else:
			print(partidoGanador)
		if(i+1 < casos):
			print()
		datos={} #restarua a vacio el diccionario de datos (persona, votos)
		candidatos={} #restarua a vacio el diccionario de candidatos (persona, partido politico)

main()