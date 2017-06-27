import fileinput

def menu():
	print "Digite uma opcao:"
	print "1 - RESOLVER o problema 1"
	print "2 - RESOLVER o problema 2"
	print "3 - RESOLVER o problema 3"
	print "4 - Sair"
	print "Escolha:"
	for line in fileinput.input():
		line = line.strip()
		if(line.isdigit()):
			return int(line)
		else:
			print line, "nao e uma opcao valida"

def main():
	option = menu()

if __name__ == '__main__':
	main()