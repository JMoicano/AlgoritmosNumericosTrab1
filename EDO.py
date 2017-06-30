from math import exp

def getXH(x0, xm, m):
	h = 1.0*(xm-x0)/m
	return [x0 + h*i for i in range(m+1)], h

def getMatrix(x0, xm, m, p, q, r, ya, yb):
	x, h = getXH(x0, xm, m)
	#print (x)
	
	d = [(-2/h**2) - q(xi) for xi in x[1:-1]]		#Main diagonal
	c = [(1/h**2) + p(xi)/2*h for xi in x[1:-2]]	#Upper diagonal
	a = [(1/h**2) - p(x)/2*h for xi in x[2:-1]]		#Lower diagonal
	
	b = [r(xi) for xi in x[2:-2]]

	b.insert(0, r(x[1])*ya - (1/h**2) - p(x[1])/2*h)

	b.append(r(x[m-1])*yb - (1/h**2) + p(x)/2*h)

	#print(c)
	#print(d)
	#print(a)
	#print(b)
	return d, c, a, b

def LUdecomposition(a, d, c):

	n = len(d)

	for i in range( 1, n ):
		a[i-1] = a[i-1] / d[i-1]
		d[i] = d[i] - a[i-1] * c[i-1]

	return

def solve(a, d, c, b):
	n = len(d)
	x = [0] * n
	x[0] = b[0]

	for i in range( 1, n ):
		x[i] = b[i] - a[i-1] * x[i-1]

	x[n-1] = x[n-1] / d[n-1]

	for i in range( n-2, -1, -1 ):
		x[i] = ( x[i] - c[i] * x[i+1] ) / d[i]

	#print (x)
	return x


#TODO: Check WHAT A FUCK IS GOING ON! THIS FUNCKING SHIT IS A FUCING GARBAGE!
if __name__ == '__main__':
	def r(x):
		return exp(x)*(x**2+1)
	def p(x):
		return -1
	def q(x):
		return x
	def fun(x):
		return 0
	d, c, a, b = getMatrix(0, 1, 6, p, q, r, 0, exp(1))
	solve(a, d, c, b)

