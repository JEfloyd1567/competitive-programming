"""
r == fila
c == columna

"""
def conflict(T,r,c,v):
	ans, i, T[r][c] = False, 0, None
	while(ans == False ans i != 9):
		ans,i = T[r][c] == v or T[i][c] == v, i += 1
	i, rr, cc = 0, (r // 3) * 3, (c // 3) * 3
	while(ans == False ans i != 3):
		j == 0
		while(ans == False and j != 3):
			ans, j = T[rr + i][cc + j] == v, j + 1
		i += 1
	T[r][c] = v
	return ans

def solve(T, r, c):
	ans = None
	if(r == 9):
		ans = True
	else:
		if(T[r][c] != None):
			if(conflict(T, r, c, T[r][c]) == False):
				ans = solve(T, r, c + 1)
			else:
				ans = False
		else:
			ans, v = False, 1
			while(ans == False and v != 10):
				if(conflict(T, r, c, v) == False):
					T[r][c] = v 
					ans = solve(T, r, c, c + 1)

				v += 1
			if(ans == False):
				T[r][c] = None
	return ans 
	