from sys import stdin
def main():
	line=stdin.readline()
	repeticiones = 0
	while(line != ""):
		string=""
		arr=[]
		arr=list(line)
		for k in range(len(arr)):
			if(arr[k] == '"'):
				repeticiones += 1
				arr[k]= "``"
				if(repeticiones == 2):
					repeticiones = 0
					arr[k]="''"
		for p in range(len(arr)):
			string=string+arr[p]
		print(string,end='')
		line=stdin.readline()
main()