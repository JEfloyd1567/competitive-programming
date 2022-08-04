from sys import stdin

def mss(A, low, hi):
    ans = None
    if low == hi:
      ans = 0
    elif low + 1 == hi:
      ans = max(0, A[low])
    else:
        mid = low + ((hi - low) >> 1)
        assert low < mid < hi
        ans = max(mss(A, low, mid), mss(A, mid, hi))
        ans = max(ans, best_crossing(A, low, mid, hi))
    return ans

def best_crossing(A, low, mid, hi):
    bl, sl, l = A[mid-1], A[mid-1], mid-2
    while l >= low:
        sl += A[l]
        bl = max(bl, sl)
        l -= 1
    br, sr, r = A[mid],A[mid],mid+1
    while r < hi:
        sr += A[r]
        br = max(br, sr)
        r += 1
    return bl + br















