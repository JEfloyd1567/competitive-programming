
from sys import stdin


def main():
	casos=int(input())
	problemas=0
	tiempo=0
	puesto=1
	diccionario={}
	for i in range(casos):
		linea = stdin.readline()
		lineaArray=linea.strip().split()
		equipo=int(lineaArray[0])
		problema=lineaArray[1]
		hora=lineaArray[2]
		estado=lineaArray[3]
		diccionario["RANK"] = puesto 
		diccionario["TEAM"] = equipo
		if(estado=='Y'):
			problemas = problemas + 1
			diccionario["PRO/SOLVED"] = problemas 
			tiempo = (int(hora[0])*60)+int(hora[2])+int(hora[3])
			diccionario["TIME"] = tiempo
		else:
			diccionario["PRO/SOLVED"] = " "
			diccionario["TIME"] = " "
	print("\n")
	for key in diccionario:
		print (key, ':',diccionario[key])

main()