from sys import stdin

letters = ['A','C','G','T']

def solve(s, k, i, m, mutations):
    if(i == 0):
        mutations.append(m)
    else:
        if(k == 0):
            solve(s, k, i - 1, s[i - 1] + m, mutations)
        else:
            solve(s, k, i - 1, s[i - 1] + m, mutations)
            for e in letters:
                if(e != s[i - 1]):
                    solve(s, k - 1, i - 1, e + m, mutations)

	
	
def main():
	cases = int(stdin.readline())
	for i in range(cases):
		n, k = map(int, stdin.readline().strip().split())
		string = stdin.readline().strip()
		mutations = list()
		solve(string, k, len(string), "", mutations)
		mutations.sort()
		print(len(mutations))
		for i in range(len(mutations)):
			print(mutations[i])
main()