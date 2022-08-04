from sys import stdin

def main():
	casos=int(input())
	urls=[]
	relevancias=[]
	for i in range(casos):
		valor=0
		urls=[]
		relevancias=[]
		for k in range(10):
			line=list(map(str,stdin.readline().strip().split()))
			url=str(line[0])
			relevancia=int(line[1])
			urls.append(url)
			relevancias.append(relevancia)
		
		for j in range(10):
			if(relevancias[j]>=valor):
				valor=relevancias[j]

		print("Case #"+str(i+1)+":")
		for t in range(10):
			if(relevancias[t]==valor):
				print(urls[t])
main()