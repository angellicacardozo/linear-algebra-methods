"""
	Coordinate format storage method for large sparse matrices
"""
def getCoordinateFormatFromMatrix(A):

	nrows = len(A)
	ncols = len(A[0])
	
	AV = [] #non zero values
	AC = [] #non zero columns
	AR = [] #non zero rows

	for i in range(nrows):
		for j in range(ncols):
			if(A[i][j] != 0):
				AV.append(A[i][j])
				AC.append(j)
				AR.append(i)

	return (AV, AC, AR)

A = [[1., 0, 0, 2., 0],
	[3., 4., 0, 5., 0],
	[6., 0, 7., 8., 9.],
	[0, 0, 10., 11., 0],
	[0, 0, 0, 0, 12.]]

print(getCoordinateFormatFromMatrix(A))