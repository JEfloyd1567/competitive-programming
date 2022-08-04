X=[(1,2),(0,3),(2,4),(3,4), (3,5),(5,8), (7,9)]
ans=[]

def phi(p, j):
  global ans
  N = len(X)
  if(j < N):
    if(X[j][0] <= p):
      #no ha encontrado un corte
      phi(p, j + 1)
    else:
      ans.append(X[j][1])
      phi(X[j][1], j + 1)

phi(-1,0)
print(ans)
