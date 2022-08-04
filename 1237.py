from sys import stdin

def solve(value, lista):
	lans = []
	ans = None
	i = 0
	while(i < len(lista) and len(lans) < 2):
		if( value >= int(lista[i][1]) and value <= int(lista[i][2])):
			lans.append(lista[i][0])
			ans = lans[0]
		i += 1
	if(len(lans) < 1):
		ans = 'UNDETERMINED'
	return ans

def main():
	cases = int(stdin.readline())
	listData = []
	for i in range(cases):
		data = int(stdin.readline())
		for _ in range(data):
			line = stdin.readline().strip().split()
			listData.append(line)
		query = int(stdin.readline())
		for _ in range(query):
			value = int(stdin.readline())
			print(solve(value,listData))
		print()
main()