"""
	Sparse Cholesky with CSR
"""

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

def dotProduct(x, y):
	dp = 0

	if not len(x)==len(y):
		return 0
		#raise ValueError('Nao e possivel realizar produto interno de x e y: larguras diferentes')

	n = len(x)
	for i in range(n):
		dp = dp + float(x[i]*y[i])

	return dp

def matrixByvector(AV, X, AR, AC):

	n = len(AR)

	y = []

	for i in range(n-1):
		k1 = AR[i]
		k2 = AR[i+1]

		y.append(dotProduct(AV[k1:k2],[X[i] for i in AC[k1:k2]]))

	return y

def getCompressedSparseRowFormatFromMatrix(A):

	nrows = len(A)
	ncols = len(A[0])

	firstocc = -1
	
	AV = [] #non zero values
	AC = [] #non zero columns
	AR = [] #pointers to the beginning of each row

	for i in range(nrows):
		for j in range(ncols):

			if(A[i][j]!=0 and firstocc==-1):
				firstocc = len(AV) # Register the non zero first occ

			if(A[i][j] != 0):				
				AV.append(A[i][j])
				AC.append(j)

		if not firstocc==-1:
			AR.append(firstocc)

		firstocc = -1

	return (AV, AC, AR)

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

def solveLy(AV, AR, AC, b):
	n = len(AR)

	y = [0 for i in range(n)]

	for i in range(n):

		if not (i+1) == n:
			k1 		= AR[i]
			k2 		= AR[i+1]
			line  	= AV[k1:k2]
			incos 	= [y[j] for j in AC[k1:k2]]
		else:
			k1 		= AR[i]
			line 	= AV[k1:]
			incos 	= [y[j] for j in AC[k1:]]


		diag  = line[len(line) - 1]
		coefs = line[:-1] # removes the last element: the element on diagonal

		y[i] = (1/float(diag))*(b[i] - dotProduct(coefs, incos[:-1]))

	return y

def solveLtx(AV, AR, AC, y):

	n = len(AR)

	x = [0 for i in range(n)]

	y.reverse()

	for i in range(n):

		if not (i+1) == n:
			k1 		= AR[i]
			k2 		= AR[i+1]
			line  	= AV[k1:k2]
			incos 	= [x[j] for j in AC[k1:k2]]
			print([x[j] for j in AC[k1:k2]])
		else:
			k1 		= AR[i]
			line 	= AV[k1:]
			incos 	= [x[j] for j in AC[k1:]]

		line.reverse() # transpose

		diag  = line[0]
		coefs = line[1:] # removes the last element: the element on diagonal

		x[i] = (1/float(diag))*(y[i] - dotProduct(coefs, incos[:-1]))

	return x.reverse()


A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]

L  	= getL(A)
csr = getCompressedSparseRowFormatFromMatrix(L)
y 	= solveLy(csr[0], csr[2], csr[1], b) # must return [0.0, 0.5, 0.5]
x 	= solveLtx(csr[0], csr[2], csr[1], y) # must return [-0.5, 0.5, 0.5]

print("Solution for x is: ", x)