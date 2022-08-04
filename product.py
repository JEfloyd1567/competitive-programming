from sys import stdin


def mss(A, low, hi):
    ans = None
    if low == hi:
      ans = 0
    elif low + 1 == hi:
      ans = A[low]
    else:
        mid = low + ((hi - low) >> 1)
        assert low < mid < hi
        ans = max(mss(A, low, mid), mss(A, mid, hi))
        ans = max(ans, best_crossing(A, low, mid, hi))
    return ans

def best_crossing(A, low, mid, hi):
    bl, sl, l = A[mid-1], A[mid-1], mid-2
    mi =  A[mid-1] #mayor izquierda
    mei= A[mid-1] #menor izquierda
    md = A[mid] #mayor derecho
    med = A[mid] #menor derecho
    tmp = 1
    tmp2 = 1
    while l >= low:
        #print("sl", sl)
        sl *= A[l]
        #print('tmp: ', tmp)
        tmp = sl
        #print("max(tmp, mi)")
        mi = max(tmp,mi)
        #print("min(tmp, mei)")
        mei = min(tmp, mei)
        l -= 1
    br, sr, r = A[mid], A[mid], mid+1
    
    while r != hi:
        #print("sr", sr)
        sr *= A[r]
        #print('tmp2: ', tmp2)
        tmp2 = sr
        #print("max(tmp2, md)")
        md = max(tmp2, md)
        #print("min(tmp2, med)")
        med = min(tmp2,med)
        #br = max(br, sr)
        r += 1

    if( (mi * md) >= (mei * med) ):
      return mi * md
    else:
      return mei * med
    
#def solve(a):
#  ans = -1
  # place your code here
 # return ans


def main():
  test = list()
  for l in stdin.readlines():
    for x in map(int, l.split()):
      if x==-999999:
        print(mss(test, 0, len(test)))
        test = list()
      else: test.append(x)
  
main()
