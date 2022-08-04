from sys import stdin


def main():
	## reomover -> "6 5 \n" : string
	line = stdin.readline()
	## .strip() -> remover "\n" de un string
	## ["6","5"] -> reomover "\n" de un string
	## map(func, container)
	## map(int, ["6","5"])->6, 5
	##p,g =map(inr, ["6","5"])-> p=6,g=5 
	p,g = map(int, line.strip().split())
	d= dict()## diccionario -> {}
	for i in range(p):
		line = stdin.readline().strip().split()
		palabra = line[0] ##-> string
		numeroFlotante = line[1] ## string "a.b"
		aux = float(numeroFlotante)## float a.b
		a=int(aux)
		b=(aux-a)*10
		d[palabra]=a*10+b
		##ejemplo
		""""
		aux= 43.8
		a=int(43.8)->43z
		b=(43.8 -43) * 10 -> (0.8)*10 -> 8
		"""
	for i in range(g):
		line=stdin.readline().strip().split()
		acum = 0
		for j in range(len(line)-1):
			if(line[j] == '<'):
				n = int(line[j+1])*10
				if(acum < n):
					print("Guess #{} was correct.".format(i+1))
				else:
					print("Guess #{} was incorrect.".format(i+1))
			elif (line[j] == '>'):
				n = int(line[j+1])*10
				if(acum > n):
					print("Guess #{} was correct.".format(i+1))
				else:
					print("Guess #{} was incorrect.".format(i+1))
			elif (line[j] == '<='):
				n = int(line[j+1])*10
				if(acum <= n):
					print("Guess #{} was correct.".format(i+1))
				else:
					print("Guess #{} was incorrect.".format(i+1))
			elif (line[j] == '>='):
				n = int(line[j+1])*10
				if(acum >= n):
					print("Guess #{} was correct.".format(i+1))
				else:
					print("Guess #{} was incorrect.".format(i+1))
			elif (line[j] == '='):
				n = int(line[j+1])*10
				if(acum == n):
					print("Guess #{} was correct.".format(i+1))
				else:
					print("Guess #{} was incorrect.".format(i+1))
			elif (line[j] != '+'):
				acum = acum + d[line[j]]

main()