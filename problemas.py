from math import exp
from EDO import *

def problem1():
	def p(x):
		return -1
	def q(x):
		return x
	def r(x):
		return ##TODO: Atualizar isso quando definir um problema
	return p, q, r

def problem2():
	def func(x):
		return 0
	return func, func, func

def problem3():
	def p(x):
		return -1
	def q(x):
		return x
	def r(x):
		return exp(x)*(x**2+1)
	return p, q, r

