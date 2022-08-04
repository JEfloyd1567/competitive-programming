def binsearch(A, low, hi):
  ans = None
  if low==hi:
    ans = False
  elif(low + 1 == hi):
    ans = A[low] == low
  else:
    mid = low + (( hi - low) >> 1) # mid = (low+hi)//2
    if A[mid] == mid:
      ans = True
    elif A[mid] < mid:
      ans = binsearch(A, mid, hi)
    else:
      ans = binsearch(A, low, mid)
  return ans

def main():
  l=[-1, 1, 2, 5, 6, 7]
  print(binsearch(l,0,len(l)))
main()