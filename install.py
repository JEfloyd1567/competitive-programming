from sys import stdin
import math


def stabs(LR):
    LR.sort() #Ordenar por menor tiempo de inicio
    N = len(LR)
    ans = 0
    lim = 0
    i = 0
    while i < N:
        ans += 1
        lim = LR[i][1]
        i += 1
        while i < N and LR[i][0] <= lim:
            if LR[i][1] < lim: 
                lim = LR[i][1]
            i += 1  
    return ans

def main():
  n, d = map(int, stdin.readline().strip().split())
  ans = None
  case = 0
  while(n != 0):
    case += 1
    A = []
    for i in range(n):
      x, y = map(int, stdin.readline().strip().split())
      if( d - y < 0 ):
        ans = -1
      else:
        x1 = x - math.sqrt(d**2 - y**2)
        x2 = x + math.sqrt(d**2 - y**2)
        A.append((x1,x2))
    if(ans != -1):
      ans = stabs(A)
      print('Case {}: {}'.format(case,ans)) 
    else:
      print('Case {}: {}'.format(case,ans))
    line=stdin.readline()
    ans = None
    n, d = map(int, stdin.readline().strip().split())
main()