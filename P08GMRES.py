# Need review

from array import *
import numpy as np

import math

def protudoMatVet(A, v):
	n=len(A)
	s=array('f', [0 for i in range(n)])

	for i in range(n): #linhas
		for j in range(len(A[i])): #colunas
			s[i] += A[i][j] * v[j]

	return s

def subtrairVetores(a,b):
	n=len(a)
	c = array('f', [0 for i in range(n)])

	for i in range(n):
		c[i]=a[i]-b[i]

	return c

def somarVetores(a,b):
	n=len(a)
	c = array('f', [0 for i in range(n)])

	for i in range(n):
		c[i]=a[i]+b[i]

	return c

def multiplicarVetores(a,b):
	n=len(a)
	c = array('f', [0 for i in range(n)])

	for i in range(n):
		c[i]=a[i]*b[i]

	return c

def norma(x):
	s=0;
	l=len(x)

	for i in range(l):
		s += x[i]**2

	return math.sqrt(s)

def calcularVetUnit(v):
	n= norma(v)
	u= array('f', [0 for i in range(len(v))])

	for i in range(len(v)):
		u[i] = v[i]/float(n)

	return u

def multiplicarEscVet(s, v):
	n= len(v)
	r = array('f', [0 for i in range(n)])

	for i in range(n):
		r[i]=s*v[i]

	return r

def prodInterno(u,v):
	l=len(u)
	p=0
	for i in range(l):
		p += u[i]*v[i]

	return p

def GMRES(A, b, x0, kmax):
	Ax0 = protudoMatVet(A,x0)
	r = subtrairVetores(b, Ax0)

	x=[]
	x.append(r) # definindo x0

	q = [0] * (kmax+1) # initializes q, nothing more than it ...
	h = [ array('f', [0 for i in range(kmax)]) for j in range(kmax+1) ] # initializer h ...

	q[0] = calcularVetUnit(r)

	for k in range(kmax):
		y = protudoMatVet(A,q[k])

		for j in range(k):
			h[j][k] = prodInterno(q[j], y)
			y = subtrairVetores(y, multiplicarEscVet(h[j][k], q[j]))

		h[k + 1][k]=norma(y)
		if h[k + 1][k] != 0 and k != kmax:
			q[k + 1] = calcularVetUnit(y)

		b = array('f', [0 for i in range(kmax + 1)])
		b[0] = norma(r)

	ck = np.linalg.lstsq(h,b)[0]

	x.append(somarVetores((multiplicarVetores(q[k],ck)), x0))

	return x

A = [[3,-1,1], [-1,3,-1],[1,-1,3]]
b = [-1,7,-7]
x = [0,0,0]

sol = GMRES(A, b, x, 10)

print("Solution for x is: ", sol)