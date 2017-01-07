from math import sqrt

def transpose(A):
	B = []
	l = len(A)
	c = len(A[0])

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

def getL(A):

	lines = len(A)
	columns = len(A[0])

	L = [[0 for j in range(columns)] for i in range(lines)]

	L[0][0] = sqrt(A[0][0])
	for i in range(1, lines, 1):
		L[i][0] = (1/float(L[0][0])) * A[i][0]

	for i in range(1, lines, 1):
		acc = 0
		for j in range(i):
			if j==0:
				acc = L[i][j]**2
			else:
				acc = acc - L[i][j]**2
		L[i][i] = sqrt(A[i][i] - acc)

		if (i+1) == lines:
			L[i][i] = 1.
			return L

		acc = 0
		for k in range(i):
			if k==0:
				acc = L[i+1][k]*L[i][k]
			else:
				acc = acc - L[i+1][k]*L[i][k]
		
		L[i+1][i] = (1/float(L[i][i]))*(A[i+1][i] - acc)

def solve(A,L):
	L  = getL(A)
	Lt = transpose(L)

	print(L,Lt)

	n = len(A)

	y = [0 for i in range(n)]
	for i in range(0,n,1):
		acc = b[i]
		for k in range(0,i,1):
			acc = acc - L[i][k]*y[k]

		y[i] = (1/float(L[i][i]))*(acc)

	x = [0 for i in range(n)]
	for i in range(n - 1, -1, -1):
		acc = y[i]
		for j in range(i + 1, n):
			acc = acc - Lt[i][j]*x[j]

		x[i] = (1/float(Lt[i][i]))*(acc)

	return x

"""
A = [[4,2,-4],[2,10,4],[-4,4,9]]
b = [0,1,0]
"""

A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]


L  = getL(A)
x = solve(A,L)

print("Solution for x is: ", x)

"""
	x1 = -0.5
	x2 = 0.5
	x3 = 0.5
"""