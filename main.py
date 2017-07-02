from problemas import *
from math import exp
import EDO

def mainMenu():
	print "Digite uma opcao:"
	print "1 - RESOLVER o problema 1"
	print "2 - RESOLVER o problema 2"
	print "3 - RESOLVER o problema 3"
	print "4 - Sair"
	while True:
		line = raw_input("Escolha: ")
		line = line.strip()
		if(line.isdigit()):
			return int(line)
		else:
			print line, "nao e uma opcao valida"

def menuArgs():
	m = raw_input("Escolha m (a discretizacao do problema): ")
	m = int(m.strip())
	ya = raw_input("Escolha valor de contorno ya (para y(0)): ")
	ya = double(ya.strip())
	yb = raw_input("Escolha valor de contorno yb (para y(1)): ")
	yb = double(yb.strip())
	return m, ya, yb


def main():
	options = {1 : problem1, 2 : problem2, 3 :problem3}
	while True:
		option = mainMenu()
		if option < 4:
			p, q, r = options[option]()
			m, ya, yb = menuArgs()
			if option == 3:
				ya, yb = 0, exp(1)
			EDO.main(m, p, q, r, ya, yb)
		else:
			break


if __name__ == '__main__':
	main()