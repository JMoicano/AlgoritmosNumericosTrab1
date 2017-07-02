from math import exp
import numpy as np

def getXH(x0, xm, m):
	h = 1.0*(xm-x0)/m
	return [x0 + h*i for i in range(m+1)], h

def getMatrix(x0, xm, m, p, q, r, ya, yb):
	x, h = getXH(x0, xm, m)
	
	d = [(-2.0/h**2) - q(xi) for xi in x[1:-1]]			#Main diagonal
	c = [(1.0/h**2) + p(xi)/2.0*h for xi in x[1:-2]]	#Upper diagonal
	a = [(1.0/h**2) - p(xi)/2.0*h for xi in x[2:-1]]	#Lower diagonal
	
	b = [r(xi) for xi in x[2:-2]]

	b.insert(0, r(x[1])*ya - (1.0/h**2) - p(x[1])/2.0*h)

	b.append(r(x[m-1])*yb - (1.0/h**2) + p(x[m-1])/2.0*h)

	return d, c, a, b, x

def LUdecomposition(a, d, c):

	n = len(d)

	for i in range( 1, n ):
		a[i-1] = a[i-1] / d[i-1]
		d[i] = d[i] - a[i-1] * c[i-1]

	return

def Gauss(d, u, l, b):
	n = len(l)
	u[0] = 1.0*u[0]/d[0]
	x = b[:]
	for i in xrange(1,n):
		m = 0

	for i in xrange(n-2,-1, -1):
		pass
	print x
	return x


def TDMA(a,b,c,f):
    a, b, c, f = map(lambda k_list: map(float, k_list), (a, b, c, f))

    alpha = [0]
    beta = [0]
    n = len(f)
    x = [0] * n

    for i in range(n-1):
        alpha.append(-b[i]/(a[i]*alpha[i] + c[i]))
        beta.append((f[i] - a[i]*beta[i])/(a[i]*alpha[i] + c[i]))
            
    x[n-1] = (f[n-1] - a[n-2]*beta[n-1])/(c[n-1] + a[n-2]*alpha[n-1])

    for i in reversed(range(n-1)):
        x[i] = alpha[i+1]*x[i+1] + beta[i+1]
    
    return x

def TDMASolve(a, b, c, d):
    n = len(a)
    xc = []
    for j in range(2, n):
        if(b[j - 1] == 0):
            ier = 1
            return
        a[j] = a[j]/b[j-1]
        b[j] = b[j] - a[j]*c[j-1]
    if(b[n-1] == 0):
        ier = 1
        return
    for j in range(2, n):
        d[j] = d[j] - a[j]*d[j-1]
    d[n-1] = d[n-1]/b[n-1]
    for j in range(n-2, -1, -1):
        d[j] = (d[j] - c[j]*d[j+1])/b[j]
    print d
    return d

def solve(a, d, c, b):
	n = len(d)
	x = [0] * n
	x[0] = b[0]

	for i in range( 1, n ):
		x[i] = b[i] - a[i-1] * x[i-1]

	x[n-1] = x[n-1] / d[n-1]

	for i in range( n-2, -1, -1 ):
		x[i] = ( x[i] - c[i] * x[i+1] ) / d[i]

	print (x)
	return x


if __name__ == '__main__':
	def r(x):
		return exp(x)*(x**2+1)
	def p(x):
		return -1
	def q(x):
		return x
	def fun(x):
		return 0
	d, c, a, b, x = getMatrix(0, 1, 10, p, q, r, 0, exp(1))
	#print(TDMA(c,a,d,b))
	#Gauss(d,c,a,b)
	#TDMASolve(a, d, c, b)
	#LUdecomposition(a, d, c)
	#adc dac cda acd dca
	#y = solve(a, d, c, b)