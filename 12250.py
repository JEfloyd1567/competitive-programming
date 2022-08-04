from sys import stdin
def main():
	i = 0;
	while(True):
		i += 1
		palabra=str(input())
		if(palabra == "#"):
			break;
		elif(palabra == "HELLO"):
			print("Case "+str(i)+":"+" "+"ENGLISH")
		elif(palabra == "HOLA"):
			print("Case "+str(i)+":"+" "+"SPANISH")
		elif(palabra == "HALLO"):
			print("Case "+str(i)+":"+" "+"GERMAN")
		elif(palabra == "BONJOUR"):
			print("Case "+str(i)+":"+" "+"FRENCH")
		elif(palabra == "CIAO"):
			print("Case "+str(i)+":"+" "+"ITALIAN")
		elif(palabra == "ZDRAVSTVUJTE"):
			print("Case "+str(i)+":"+" "+"RUSSIAN")
		else:
			print("Case "+str(i)+":"+" "+"UNKNOWN")
main()