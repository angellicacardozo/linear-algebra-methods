def JCB(A,b,x):
	rows	= len(A[0])
	lines	= len(A)
	xn		= [0 for i in range(lines)]

	for i in range(lines):
		for j in range(rows):
			if(i!=j):
				xn[i] = xn[i] - (A[i][j]*x[j])
		xn[i] = (1/float(A[i][i])) * (b[i] + xn[i])

	return xn

A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]
x = [0,0,0]
e = 0.01

x = JCB(A, b, x)
x = JCB(A, b, x)

print(x)