# @description Multiplies a scalar by a vector
def stv(s, v):
	l=len(v)
	x=[1 for i in range(l)]

	for i in range(l):
		x[i]=s*v[i]

	return x

def add(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] + y[i]

	return z

def sub(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] - y[i]

	return z

def mtv(A, x):
	m=len(A)
	n=len(x)

	y=[0 for i in range(m)]

	for i in range(m):
		for j in range(n):
			# print('Multiplicando A[' + str(i) + '][' + str(j) + '] por x['+ str(i) + ']')
			y[i] += A[i][j]*x[j]

	return y

def jacobi(A,b,x):
	rows	= len(A[0])
	lines	= len(A)
	xn		= [0 for i in range(lines)]

	for i in range(lines):
		for j in range(rows):
			if(i!=j):
				xn[i] = xn[i] - (A[i][j]*x[j])
		xn[i] = (1/float(A[i][i])) * (b[i] + xn[i])

	return xn

def Multigrid(A,b,x):

	# pre-smoothing
	for i in range(5):
		x = add(stv(0.8,jacobi(A, b, x)),stv(0.2,x))

	# residual equation
	r = sub(b, mtv(A,x))

	# perform restriction

	return (x, r)

A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]
x = [0,0,0]
e = 0.01

x = Multigrid(A, b, x)

print(x)