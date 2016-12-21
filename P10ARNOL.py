from array import *
import math

def produtoMatVet(A, v):
	n=len(A)
	s=array('f', [0 for i in range(n)])

	for i in range(n): #linhas
		for j in range(len(A[i])): #colunas
			s[i] += A[i][j] * v[j]

	return s

def prodInterno(u,v):
	l=len(u)
	p=0
	for i in range(l):
		p += u[i]*v[i]

	return p

def subtrairVetores(a,b):
	n=len(a)
	c = array('f', [0 for i in range(n)])

	for i in range(n):
		c[i]=float(a[i])-float(b[i])

	return c

def multiplicarEscVet(s, v):
	n= len(v)
	r = array('f', [0 for i in range(n)])

	for i in range(n):
		r[i]=s*v[i]

	return r

def norma(x):
	s=0;
	l=len(x)

	for i in range(l):
		s += x[i]**2

	return math.sqrt(s)

def eOrthogonal(u,v):
	n=len(u)
	z=0
	EPSILON=0.0001
	for i in range(n):
		z = z + (u[i] * v[i])
		
	if(abs(z)<EPSILON):
		return 0

	return z

def formatarMatriz(matrix):
	s = [[str(e) for e in row] for row in matrix]
	lens = [max(map(len, col)) for col in zip(*s)]
	fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
	table = [fmt.format(*row) for row in s]
	print '\n'.join(table)

def Arnoldi(A,b,m):

	v=[[0 for j in range(m)] for i in range(m+1)]
	w=[[0 for j in range(m)] for i in range(m)]
	h=[[0 for j in range(m)] for i in range(m+1)]

	EPSILON=0.0001
	j=0

	v[0]=multiplicarEscVet(1/float(norma(b)), b)

	while j <= m:
		w[j]=produtoMatVet(A,v[j])
		for i in range(j+1):
			h[i][j]=prodInterno(w[j],v[i])
			w[j]=subtrairVetores(w[j], multiplicarEscVet(h[i][j],v[i]))

		h[j+1][j]=norma(w[j])

		if abs(h[j+1][j])<EPSILON:
			j=m+1
		else:
			v[j+1]=multiplicarEscVet(1/float(h[j+1][j]),w[j])
			j = j + 1

	print("--------------------------------------------")
	print("Conjunto V")
	formatarMatriz(v)

	print("--------------------------------------------")
	print("Conjunto W")
	formatarMatriz(w)

	print("--------------------------------------------")
	print("Matriz de Heisenberg")
	formatarMatriz(h)
	print("--------------------------------------------")

	print("Verificando se os vetores sao ortogonais")
	n=len(v)
	for j in range(n):
		for i in range(n):
			if(i!=j):
				print("Verificando se v["+str(j)+"] e ortogonal com v["+str(i)+"]: " + str(eOrthogonal(v[j],v[i])))

A = [[3,2,4],[1,1,2],[4,3,2]]
b = [1,2,3]

#A = [[3,-2],[-5,4]]
#b = [6,8]

Arnoldi(A,b,3)