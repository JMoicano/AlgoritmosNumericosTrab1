def getXH(a, b, m):
	h = 1.0*(b-a)/m
	return [a + h*i for i in xrange(m+1)], h

def getLine(p, q, h, x):
	line = []
	line.append((1/h**2) - p(x)/2*h)
	line.append((-2/h**2) - q(x))
	line.append((1/h**2) + p(x)/2*h)
	return line

def getMatrix(a, b, m, p, q, r, ya, yb):
	x, h = getXH(a, b, m)
	
	MatA = [getLine(p, q, h, xi) for xi in x[2:-2]]
	
	firstLine = []
	firstLine.append((-2/h**2) - q(x[1]))
	firstLine.append((1/h**2) + p(x[1])/2*h)
	MatA.insert(0, firstLine)
	
	lastLine = []
	lastLine.append((1/h**2) - p(x[m-1])/2*h)
	lastLine.append((-2/h**2) - q(x[m-1]))
	MatA.append(lastLine)

	MatB = [r(xi) for xi in x[2:-2]]

	MatB.insert(0, r(x[1])*ya - (1/h**2) - p(x[1])/2*h)

	MatB.append(r(x[m-1])*yb - (1/h**2) + p(x)/2*h)

	return MatA, MatB