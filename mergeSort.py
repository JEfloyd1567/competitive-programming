from sys import stdin
import random

def mergeSort(A, low, hi):
	if(low+1 < hi):
		mid = low + ((hi - low) >> 1)
		#print("low = ", str(low), " mid = ", str(mid))
		#print(A[low:mid])
		mergeSort(A, low, mid)
		#print("mid = ", str(mid), " hi = ", str(hi))
		#print(A[mid:hi])
		mergeSort(A, mid, hi)
		#print("Merge = low: " + str(low) + " mid: "+ str(mid) + " hi: ", str(hi))
		merge(A, low, mid, hi)
	return A


def merge(A, low, mid, hi):
	global tmp, contador
	for i in range(low, hi):
		tmp[i] = A[i] 
	l = low
	r = mid
	for n in range(low,hi):
		#print("n =", str(n))
		#print(str(l), " == ", str(mid))
		if(l == mid):
			#print("A[n] = ", " tmp[r] = ", str(tmp[r]))
			A[n] = tmp[r]
			#print("A:", A)
			r = r + 1
			#print("r == ", str(r), " hi= ", str(hi))
		elif(r == hi):
			#print("A[n] = ", " tmp[l] ", str(tmp[l]))
			A[n] = tmp[l]
			#print("A:", A)
			l = l + 1
		else:
			#print("tmp[l] <= ", str(tmp[l]), " tmp[r] ", str(tmp[r]))
			if(tmp[l] <= tmp[r]):
				#print("A[n] = ", " tmp[l] ", tmp[l])
				A[n] = tmp[l]
				#print("A:", A)
				l += 1
			else:
				#print("A[n] = ", "tmp[r]= ", str(tmp[r]))
				A[n] = tmp[r]
				#print("A:", A)
				r += 1
				contador += r - n - 1
	print(contador)
def main():
	global tmp, A, contador
	contador = 0
	A = [1]
	#for i in range(5):
	#	A.append(random.randint(0,100))
	print("antes de ordenar:", A)
	tmp = [0 for _ in range(len(A))]
	mergeSort(A, 0, len(A))
	print("ordenado:", A)

main()