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

def norm(x):
	s=0;
	l=len(x)

	for i in range(l):
		s += x[i]**2

	return math.sqrt(s)

def getLambda(r,y,d,k):

	dT=transpose(d, len(d), 1)
	rT=transpose(r[k], len(r[k]), 1)
	rNorm=norm(r[k])

	dLambda = (((1/float(multiply(dT, y)[0]))))
	dLambda = dLambda * (multiply(rT,d)[0])
	dLambda = dLambda * ((1/float(norm(r[k]))))
	dLambda = dLambda * multiply(rT,y)[0]

	return 1 + dLambda

def ConjGrad(A,b, guess, kmax, tol):
	k=0;
	r=[[] for i in range(kmax)] # Initializes the residual array
	r[k]= subtract(b, multiply(A, guess))
	rT=transpose(r[k], len(r[k]), 1)
	d=list(r[k])
	delta=multiply(rT,r[k])
	deltaZ=list(delta)

	y=multiplyScalarByVector(-1, r[k])
	dLambda=1
	EPSILON=0.0001
	conjugCondition=1

	while k<kmax and delta[0] > (tol**2)*deltaZ[0]:
		q=multiply(A,d)
		dT=transpose(d, len(d), 1)
		alpha=delta[0]/float(multiply(dT,q)[0])
		guess=add(guess, multiplyScalarByVector(alpha, d))

		if k % 50 ==0:
			r[k]= subtract(b, multiply(A, guess))
		else:
			r[k]= subtract(r[k-1], multiplyScalarByVector(alpha, q))

		tmpDelta=list(delta)
		rT=transpose(r[k], len(r[k]), 1)
		delta=multiply(rT,r[k])
		beta=delta[0]/float(tmpDelta[0])

		if k >=1 :
			conjugCondition= multiply(rT,y)[0]
			if conjugCondition< EPSILON:
				conjugCondition=0
		
		if conjugCondition > 0:
			d=add(r[k], multiplyScalarByVector(beta, d))
		else :
			dLambda=getLambda(r,y,d,k)
			d=add(multiplyScalarByVector(dLambda, r[k]), multiplyScalarByVector(beta, d))

		if k >=1 :
			y=subtract(r[k],r[k-1])
		
		k +=1

	return guess

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