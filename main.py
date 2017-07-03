from problemas import *
from math import exp
import matplotlib.pyplot as plt
from math import exp

def getXH(m):
	'''
	Get list of the m+1 subinterval of x and the size of h
	'''
        h = 1.0/m
        return [h*i for i in range(m+1)], h

def getMatrix(m, p, q, r, ya, yb):
	'''
	Get the tridiagona matrix in form of three lists
	'''
        x, h = getXH(m)
        
        b = [(-2.0/h**2) + q(xi) for xi in x[1:-1]]             #Main diagonal
        c = [(1.0/h**2) + p(xi)/2.0*h for xi in x[1:-2]]        #Upper diagonal
        a = [(1.0/h**2) - p(xi)/2.0*h for xi in x[2:-1]]        #Lower diagonal
        
        d = [r(xi) for xi in x[2:-2]]

        d.insert(0, r(x[1]) - ((1.0/h**2) - p(x[1])/2.0*h)*ya)

        d.append(r(x[m-1]) - ((1.0/h**2) + p(x[m-1])/2.0*h)*yb)

        return a, b, c, d, x

def Gauss(d, u, l, b):
	'''
	The Gaussian method for a tridiagonal matrix
	'''
        s = []
        n = len(l)
        for i in xrange(n-1):
                m = l[i]/d[i]
                l[i] = 0
                d[i+1] = d[i+1] - m * u[i]
                b[i+1] = b[i+1] - m * b[i]

        for i in xrange(n-1,-1, -1):
                m = u[i]/d[i+1]
                u[i] = 0
                b[i] = b[i] - m * b[i+1]

        for i in xrange(n+1):
                s.append(b[i]/d[i])

        return s

def run(m, p, q, r, ya, yb):
	'''
	Given a problem, solve it
	'''
        l, d, u, b, x = getMatrix(m, p, q, r, ya, yb)
        y = [ya] + Gauss(d, u, l, b) + [yb]
        return x, y

def problem1():
	'''
	Definition of the Problem 1
	'''
	def p(x):
		return -1
	def q(x):
		return x
	def r(x):
		return 2*x
	return p, q, r

def problem2():
	'''
	Definition of the Problem 2
	'''
	def func(x):
		return 0
	return func, func, func

def problem3():
	'''
	Definition of the Problem 3
	'''
	def p(x):
		return -1
	def q(x):
		return x
	def r(x):
		return exp(x)*(x**2+1)
	return p, q, r

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
	ya = float(ya.strip())
	yb = raw_input("Escolha valor de contorno yb (para y(1)): ")
	yb = float(yb.strip())
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
			x, y = run(m, p, q, r, ya, yb)
			print "Para os valores de X:", x
			print "Temos Y:", y
			plt.plot(x,y)
			plt.show()
		else:
			break


if __name__ == '__main__':
	main()