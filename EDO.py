from math import exp
import matplotlib.pyplot as plt

def getXH(m):
        h = 1.0/m
        return [h*i for i in range(m+1)], h

def getMatrix(m, p, q, r, ya, yb):
        x, h = getXH(m)
        
        b = [(-2.0/h**2) + q(xi) for xi in x[1:-1]]             #Main diagonal
        c = [(1.0/h**2) + p(xi)/2.0*h for xi in x[1:-2]]        #Upper diagonal
        a = [(1.0/h**2) - p(xi)/2.0*h for xi in x[2:-1]]        #Lower diagonal
        
        d = [r(xi) for xi in x[2:-2]]

        d.insert(0, r(x[1]) - ((1.0/h**2) - p(x[1])/2.0*h)*ya)

        d.append(r(x[m-1]) - ((1.0/h**2) + p(x[m-1])/2.0*h)*yb)

        return a, b, c, d, x

def TDMA(a,b,c,d):
        a.insert(0, 0.0)
        c.append(0.0)
        n = len(b)

        c[0] = c[0]/b[0]
        d[0] = d[0]/b[0]

        for i in xrange(1,n-2):
                m = b[i] - a[i] *c[i-1]
                c[i] = c[i]/m
                d[i] = (d[i] - a[i] *d[i-1])/m

        d[-1] = (d[-1] - a[-1] * d[-2])/(b[-1] - a[-1] * c[-2])

        x = d[:]

        for i in xrange(-2, 0, -1):
                x[i] = d[i] - c[i] *x[i+1]
        return x

def Gauss(d, u, l, b):
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

        print s
        return s

def main(m, p, q, r, ya, yb):
        d, c, a, b, x = getMatrix(m, p, q, r, ya, yb)

if __name__ == '__main__':
        def r(x):
                return exp(x)*(x**2+1)
        def p(x):
                return -1
        def q(x):
                return x
        def fun(x):
                return 0
        a, b, c, d, x = getMatrix(10, p, q, r, 0, exp(1))
        #print(TDMA(a,b,c,d))
        s = Gauss(b,c,a,d)
        s.insert(0,0)
        s.append(exp(1))
        plt.plot(x,s)
        plt.show()
        #TDMASolve(a, d, c, b)
        #LUdecomposition(a, d, c)
        #adc dac cda acd dca
        #y = solve(a, d, c, b)
