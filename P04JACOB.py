import math

def subtract(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= float(x[i] - y[i])

	return z

def calc(A,b,x):
	rows	= len(A[0])
	lines	= len(A)
	xn		= [0 for i in range(lines)]

	for i in range(lines):
		for j in range(rows):
			if(i!=j):
				xn[i] = xn[i] - (A[i][j]*x[j])
		xn[i] = (1/float(A[i][i])) * (b[i] + xn[i])

	return xn

def convergePorLinhas(A):
	lines = len(A)
	columns = len(A[0])
	sums = [0 for i in range(lines)]

	for i in range(lines):
		for j in range(columns):
			if(i!=j):
				sums[i] = sums[i] + abs(A[i][j])
		sums[i] = (1/float(abs(A[i][i]))) * sums[i]

	return (max(sums) < 1)

def norma(x):
	s=0;
	l=len(x)

	for i in range(l):
		s += x[i]**2

	return math.sqrt(s)

def convergePorNorma(x, k, eps):
	EPSILON=0.0001
	return (norma(subtract(x[k-1], x[k])) < eps)

def height(m):
  return len(m)

def JCB(A, b, x0=None, eps=0.000001, max_iteration=1000):

	if not convergePorLinhas(A):
		raise ValueError('Nao converge por linhas :( ')

	x = []
	x.append(calc(A, b, x0))

	k = 0
	while k < max_iteration:

		x.append(calc(A, b, x[k]))

		if convergePorNorma(x, k, eps):
			print("Rodou em " + str(k) + " iteracoes")
			return x[k]

		k = k + 1

	raise ValueError('Nao converge por iteracao :( ')


"""
A = [[3,-1,1,-1], [-1,3,-1,7],[1,-1,3,-7]]
s = JCB(A)
"""

"""
    x1 = 1
    x2 = 2.2
    x3 = -2.2
"""

"""
A = [[4,3.2,0.5,9.2],[2.2,3,-0.3,0.9],[-3.1,-0.2,4,7]]
s = JCB(A)
"""
"""
A = A = [[1,-1,2,0], [-1,5,-4,1],[2,-4,6,0]]
s = JCB(A)
"""

A = [[10,2,1],[1,5,1],[2,3,10]]
b = [1,1,2]
x0 = [0,0,0]

s = JCB(A, b, x0)

print("Solution for x is: ", s)

