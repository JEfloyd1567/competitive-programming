from sys import stdin

def main():
	cases=int(input())
	print("Lumberjacks:")
	for i in range(cases):
		arr=list(map(int,stdin.readline().strip().split()))
		arr2=list(arr)
		arr2.sort()
		#aqui se ordena de manera descendente
		arr3=list(arr)
		arr3.sort(reverse=True)
		#comparacion del arreglo 
		if(arr==arr2 or arr3==arr):
  			print("Ordered")
		else:
  			print("Unordered")
main()