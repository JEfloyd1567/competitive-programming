from sys import stdin
import math
def solve(listt):
	ans = None
	minim = min(listt)
	maxi = max(listt)
	for i in range(len(listt)):
		if(minim < listt[i] and maxi > listt[i]):
			ans = listt[i]
	return ans

def main():
	cases = int(stdin.readline())
	print(cases)
	case = 0
	for i in range(cases):
		case += 1
		listt = list(map(int,stdin.readline().strip().split()))
		ans = solve(listt)
		print('Case {}: {}'.format(case,ans))
main()