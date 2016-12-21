from pprint import pprint
 
def matrixMul(A, B):
    TB = zip(*B)
    return [[sum(ea*eb for ea,eb in zip(a,b)) for b in TB] for a in A]
 
def pivotize(m):
    """Creates the pivoting matrix for m."""
    n = len(m)
    ID = [[float(i == j) for i in xrange(n)] for j in xrange(n)]
    for j in xrange(n):
        row = max(xrange(j, n), key=lambda i: abs(m[i][j]))
        if j != row:
            ID[j], ID[row] = ID[row], ID[j]
    return ID
 
def lu(A):
    """Decomposes a nxn matrix A by PA=LU and returns L, U and P."""
    n = len(A)
    L = [[0.0] * n for i in xrange(n)]
    U = [[0.0] * n for i in xrange(n)]
    P = pivotize(A)
    A2 = matrixMul(P, A)
    for j in xrange(n):
        L[j][j] = 1.0
        for i in xrange(j+1):
            s1 = sum(U[k][j] * L[i][k] for k in xrange(i))
            U[i][j] = A2[i][j] - s1
        for i in xrange(j, n):
            s2 = sum(U[k][j] * L[i][k] for k in xrange(j))
            L[i][j] = (A2[i][j] - s2) / U[j][j]
    return (L, U, P)

A = [[4,3,2], [3,2,4], [1,1,2]]
b = [1,2,3]

L  = lu(A)[0]
U  = lu(A)[1]

n = len(A)

# (5) Perform substitutioan Ly=b
y = [0 for i in range(n)]
for i in range(0,n,1):
	y[i] = b[i]/float(L[i][i])
	for k in range(0,i,1):
		y[i] -= y[k]*L[i][k]

# (6) Perform substitution Ltx=y
x = [0 for i in range(n)]
for i in range(n - 1, -1, -1):
	x[i] = y[i]/float(U[i][i])
	for j in range(i + 1, n):
		x[i] -= x[k]*U[i][k]

print(x)