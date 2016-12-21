# Need review

import math

# @description Multiplies a matrix by a vector (one column matrix)
def multiply(A, x):
	m=len(A)
	n=len(x)

	y=[0 for i in range(m)]

	for i in range(m):
		for j in range(n):
			# print('Multiplicando A[' + str(i) + '][' + str(j) + '] por x['+ str(i) + ']')
			y[i] += A[i][j]*x[j]

	return y

# @description Subtract y from x (x - y) where both x and y are vectors
def subtract(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] - y[i]

	return z

# @description transpose a given matrix A
def transpose(A, l, c):
	B=[]

	if(c==1):
		# A is a vector
		for i in range(c):
			B.append([])
			for j in range(l):
				B[i].append(A[j])
	else:
		for i in range(c):
			B.append([])
			for j in range(l):
				B[i].append(A[j][i])

	return B

# @description Subtract y from x (x - y) where both x and y are vectors
def add(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] + y[i]

	return z

# @description Multiplies a scalar by a vector
def multiplyScalarByVector(s, v):
	l=len(v)
	x=[1 for i in range(l)]

	for i in range(l):
		x[i]=s*v[i]

	return x

def err_norm(r):
	summ = 0;

	for i in range(len(r)):
		summ += r[i]*r[i]

	summ = math.sqrt(summ)

	if(summ < 0.01):
		return 0

	return summ

def ConjGrad(A,b, guess, kmax, tol):
	d = []
	r = []
	x = []
	alpha = []

	d.append(subtract(b, multiply(A, guess)))
	r.append(d[0])

	x.append(guess)

	k = 0
	while k<kmax and err_norm(r[k]) > tol:
		rT=transpose(r[k], len(r[k]), 1)
		dT=transpose(d[k], len(d[k]), 1)
		Ad=multiply(A,d[k])

		alpha.append((1/float(multiply(dT,Ad)[0])) * multiply(rT,r[k])[0])

		x.append(add(x[k], multiplyScalarByVector(alpha[k],d[k])))
		r.append(subtract(r[k] , multiplyScalarByVector(alpha[k],Ad)))

		beta = 1/float(multiply(rT,r[k])[0])
		rT = transpose(r[k + 1], len(r[k + 1]), 1)
		beta = beta * multiply(rT,r[k + 1])[0]

		betaD = multiplyScalarByVector(beta,d[k])
		d.append(add(r[k + 1], betaD))

		k += 1

	return x[k]


A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]
x = [0,0,0]
e = 0.01

sol = ConjGrad(A, b, x, 10, e)

print("Solution for x is: ", sol)

"""
	x1 = 0.5
	x2 = 0.5
	x3 = -0.5
"""