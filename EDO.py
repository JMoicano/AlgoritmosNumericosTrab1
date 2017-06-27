def getXH(a, b, m):
	h = 1.0*(b-a)/m
	return [a + h*i for i in xrange(m+1)], h

def getLine(p, q, h, x):
	line = []
	line.append((1/h**2) - p(x)/2*h)
	line.append((-2/h**2) - q(x))
	line.append((1/h**2) + p(x)/2*h)
	return line

def getMatrix(a, b, m, p, q):
	x, h = getXH(a, b, m)
	return [getLine(p, q, h, xi) for xi in x[1:-1]]