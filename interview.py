from sys import stdin,setrecursionlimit

setrecursionlimit(10**9)

mem={}

def trib(n, back):
	global count
	suma = 0
	count += 1
	if(n <= 0):
		return 0
	if(n == 1):
		return 1
	for i in range(1, back + 1):
		suma += trib(n - i, back)
	return suma


def trib_memo(n, back):
	ans = 0
	if((n, back) in mem):
		ans = mem[(n, back)]
	else:
		if(n <= 1):
			return 1
		else:
			ans += 1
			for i in range(1, back + 1):
				ans += trib_memo(n - i, back)
		mem[(n, back)] = ans
	return ans


def main():
	n, k = map(int, stdin.readline().strip().split())
	casos = 0
	while(n < 61):
		casos += 1
		print("Case " + str(casos) + ":", str(trib_memo(n, k)))
		n, k = map(int, stdin.readline().strip().split())
main()