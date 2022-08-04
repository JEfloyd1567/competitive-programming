from sys import stdin

def solve(word, pattern):
	'''
	reccorrer el patron y se tiene guardada la password, recibe pos del patrony lo que se lleva acomulado de la password,
	cuando ya se reccorre hasta el final, no esta hasta el final.
	si no ha llegado al final, se tinen w posibilidades, si es un 0, toca probar hasta el 9
	si es un # pero ahora con cada palabra del diccionario
	'''
	
def main():
	line = stdin.readline().strip().split()
	while(line != ''):
		number = int(line[0])
		words=[]
		for i in range(number):
			word = stdin.readline().strip().split()
			words.append(word)
		numberP = int(stdin.readline())
		for i in range(numberP):
			patternList = stdin.readline().strip().split()
			pattern = str(patternList[0])
		print(words)
		print(pattern)
		line = stdin.readline().strip().split()
main()