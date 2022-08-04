from sys import stdin


def binary_search(A, x, low, hi):
    ans = None
    if (low + 1 == hi):
    	ans = low
    else:
        mid = ((low + hi) >> 1)
        if (A[mid] <= x):
        	ans = binary_search(A, x, mid, hi)
        else:
        	ans = binary_search(A, x, low, mid)
    return ans

def solucion(x):
	global dic
	#print(x)
	flag = True
	ans = []
	c = 1
	aux = None
	#print(dic)
	if(x[0] in dic):
		ans.append(dic[x[0]][0])
		aux = int(ans[0])
	else:
		flag = False
	while(flag and c < len(x)):
		if(x[c] in dic):
			aux2 = binary_search(dic[x[c]], aux , 0, len(dic[x[c]]))
			if(dic[x[c]][aux2] > aux):
				aux = dic[x[c]][aux2] 
			else:
				if(aux2 + 1 < len(dic[x[c]])):
					aux2 += 1
					aux2 = dic[x[c]][aux2]
					if(aux2 > aux):
						aux = aux2 
					else:
						flag = False
						ans = []
				else:
					flag = False
					ans = []
		else:
			flag = False
			ans = []
		c += 1
	if(flag):
		ans.append(aux)
	return ans

def main():
	global dic
	s = str(stdin.readline().strip())
	dic = {}
	for i in range(len(s)):
		if(s[i] in dic):
			dic[s[i]].append(i)
		else:
			dic[s[i]]=[i]
	q = int(stdin.readline())
	for i in range(q):
		x = str(stdin.readline().strip())
		ans = solucion(x)
		if(len(ans)):
			print("Matched "+str(ans[0])+" "+str(ans[1]))
		else:
			print("Not matched")

main()
