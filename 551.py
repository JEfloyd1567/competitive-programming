#Juan Esteban Floyd J
#solucion al problema 551 judge online (https://onlinejudge.org/external/5/551.pdf)
from sys import stdin

def inverso(bracket):
	#esta funcion retorna el inverso de cualquiera de los brackets del problema
	ans = None
	if (bracket == ')'): ans = '('
	elif (bracket == '*)'): ans = '(*'
	elif (bracket == ']'): ans = '['
	elif (bracket == '}'): ans = '{'
	elif (bracket == '>'): ans = '<'
	return ans

def solucion(expresion):
	
	ans, flag = 'YES', True
	i, k = 0, 0
	pila = []
	while( flag and i < len(expresion) ): #si la bandera es verdadera y todavia el i es una pos valida en la expresion
		k += 1 #aumenta k, K ES POS DEL STRING
		if (expresion[i] =='[' or expresion[i] ==  '{' or expresion[i] == '<' or expresion[i] == '('): #si el string de entrada es algun bracket que abre 
			if (expresion[i] == '(' and i+1 < len(expresion) and expresion[i+1] == '*'): #si es un '(' y su siguiente poision es valida, ademas de ser un '*' 
				i += 1 #aumente el iterador
				pila.append('(*') #agregueme a la pila, '(*'
			else:
				pila.append(expresion[i]) #si no es un '(*', agregueme cualquier otro bracket 

		elif (expresion[i] == ']' or expresion[i] =='}' or expresion[i] =='>' or expresion[i] =='*' or expresion[i] ==')'): #en el caso en que sea un bracket que cierra
			if (len(pila) > 0): #si la pila no esta vacia
				if (expresion[i] == '*'): #si encuentra un '*'
					if (i+1 < len(expresion) and expresion[i+1] == ')'): #si todavia el i es una pos valida y al '*' le sigue un ')'
						if (inverso('*)') == pila[-1]): #si el tope de pila es igual a tope, en este verfica si el tope de pila es '(*'
							i += 1 #aumenta el iterador
							pila.pop() #lo saca de la pila
						else:
							ans = 'NO '+ str(k)
							flag = False
				else:
					if (inverso(expresion[i]) == pila[-1]): #si no es un asterisco, entonces verifica si el tope de la pila es el inverso de otro bracket
						pila.pop() #si es el inverso de algun bracket, saquelo de la pila
					else: 
						ans = 'NO '+ str(k) #si no es el inverso, hay un error en la pos k del string
						flag = False 

			elif (len(pila) <= 0): #si la pila todavia tiene elementos
				if (expresion[i] != '*'): #si su posicion es diferente de un aterisco
					ans = 'NO '+ str(k) #hay un error en la pos k del string
					flag =  False
				elif (i+1 < len(expresion) and expresion[i+1] == ')'): #si la pos i+1 es valida, y depues del '*' hay un ')'
					ans = 'NO '+ str(k)
					flag =  False
		i += 1

	if (len(pila) > 0 and flag): #si todavia hay elementos en la pila y la bandera es verdadera
		ans = 'NO '+ str(k+1) #hay un error en la pos k + 1 del string
		flag =  False
	
	return ans

def main():

	lineas = stdin.readlines() #lee todas las lineas
	lineas[-1] = lineas[-1] + '\n' if lineas[-1][-1] != '\n' else lineas[-1] #agrega un salto de linea si no lo tiene a cada linea
	lineas.reverse() #invierte todas las lineas
	while( len(lineas) > 0 ):
		linea = lineas.pop()[:-1]	#elimina el ultimo caracter, revisa cada expresion 
		print(solucion(linea))

main()