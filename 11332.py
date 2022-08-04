def main():
	while(True):
		contador=0
		numero=int(input())
		if(numero == 0):
			break
		elif(numero < 10):
			print(numero)
		else:
			contador = numero
			while(contador > 9):
				contador = 0
				while(numero > 0):
					contador = contador + (numero % 10)
					numero = numero // 10
				numero = contador
			print(contador)

main()