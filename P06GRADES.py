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

def multiplyScalarByVector(s, v):
	l=len(v)
	x=[1 for i in range(l)]

	for i in range(l):
		x[i]=s*v[i]

	return x


# @description Subtract y from x (x - y) where both x and y are vectors
def subtract(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] - y[i]

	return z

# @description Subtract y from x (x - y) where both x and y are vectors
def add(x, y):
	n=len(y)
	z=[0 for i in range(n)]

	for i in range(n):
		z[i]= x[i] + y[i]

	return z

def norm(x):
	s=0;
	l=len(x)

	for i in range(l):
		s += x[i]**2

	return math.sqrt(s)

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

def GradDesc(A, b, guess, tol):

	k=0;
	r=[0 for i in range(len(guess))] # Initializes the residual array
	y=[]

	r=subtract(b, multiply(A, guess))

	#print(" The norm is " + str(norm(r)))

	while(norm(r) > tol):
		rT=transpose(r, len(r), 1)
		Ar=multiply(A,r)
		alpha=multiply(rT, r)[0]/float(multiply(rT, Ar)[0])
		#print(" Alpha is " + str(multiply(rT, r)[0]) + "/" +str(multiply(rT, Ar)[0]) + ", thus: " + str(alpha))
		guess=add(guess, multiplyScalarByVector(alpha, r))

		k += 1
		r=subtract(b, multiply(A, guess))
		#print(" The norm is " + str(norm(r)))

	return guess

A = [[1,-1,2], [-1,5,-4],[2,-4,6]]
b = [0,1,0]
x = [0,0,0]
e = 0.00001

sol = GradDesc(A, b, x, e)

print("Solution for x is: ", sol)

"""
	x1 = 0.5
	x2 = 0.5
	x3 = -0.5
"""

#print(GradDesc([[3,-1,1], [-1,3,-1],[1,-1,3]],[-1,7,-7],[0,0,0], 0.01))