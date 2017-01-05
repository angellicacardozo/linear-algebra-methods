"""
	Implementing the Compressed Sparse Row format
"""

def dotProduct(x,y):
	dp = 0

	if not len(x)==len(y):
		raise ValueError('Nao e possivel realizar produto interno de x e y: larguras diferentes')

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

A = [[1., 0, 0, 2., 0],
	[3., 4., 0, 5., 0],
	[6., 0, 7., 8., 9.],
	[0, 0, 10., 11., 0],
	[0, 0, 0, 0, 12.]]

print(getCompressedSparseRowFormatFromMatrix(A))