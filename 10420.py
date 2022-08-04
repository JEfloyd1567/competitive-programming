from sys import stdin
from collections import deque
def main():
	cases = int(stdin.readline())
	dic = {}
	subline=[]
	sett={}
	lista=deque()
	for i in range(cases):
		aux = ''
		line = stdin.readline().strip().split()
		subline.extend(line[1:])
		for word in subline:
			aux += word
			aux += ' '
		#print('aux al inicio',aux)		
		if(line[0] in dic):
			dic[line[0]].append(aux)
		else:
			dic[line[0]]=[aux]
		#aux = ""
		#print('aux al final:',aux)
	for key in dic:
		lista.appendleft((key,len(dic[key])))
	for i in range(len(lista)):
		print(lista[i][0],lista[i][1])
main()