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
 
 
def LFactor(A):
    L = [[0.0] * len(A) for _ in xrange(len(A))]
    for i in xrange(len(A)):
        for j in xrange(i+1):
            s = sum(L[i][k] * L[j][k] for k in xrange(j))
            L[i][j] = sqrt(A[i][i] - s) if (i == j) else \
                      (1.0 / L[j][j] * (A[i][j] - s))
    return L

A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]

L  = LFactor(A)
Lt = transpose(L)

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
	x[i] = y[i]/float(Lt[i][i])
	for j in range(i + 1, n):
		x[i] -= x[k]*Lt[i][k]



print("Solution for x is: ", x)


"""
	x1 = 0.5
	x2 = 0.5
	x3 = -0.5
"""