import sys
mem = dict()
sys.setrecursionlimit(1000000000)
tab = [None for _ in range(N)]

def fibo(n):
	ans = None
	if (n < 2):
		ans = n 
	else:
		ans = fibo(n - 1) + fibo(n - 2)
	return ans

def fibo_memorizacion(n, mem):
	"""
	python, programacion dinamica, tecnica de memorizacion
	"""
	ans = None
	if(n in mem):
		ans = mem[n]
	else:
		if(n < 2):
			mem[n] = n
		else:
			mem[n] = fibo_memorizacion(n-1, mem) + fibo_memorizacion(n-2, mem)
			ans = mem[n]
	return ans 
 
def tabular():
	tab[0] = 0
	tab[1] = 1
	for i in range(2, N):
		tab[i] = tab[i - 1] + tab[i - 2]

def fibo_tabulacion(n):
	return tab[n]

def fibo_opt(N):
	if (N == 0):
		ans = 0
	elif (N == 1):
		ans = 1
	else:
		a = 0
		b = 1
		c = None
		for i in range(2, N + 1):
			c = a + b 
			a = b
			b = c
		ans = c 

prueba=int(input("ingrese un valor:"))
print(fibo_memorizacion(prueba, mem))